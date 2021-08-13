#Ranking rate
from scipy.sparse import data
from valuerate.models import *
from django.db.models import Max, Min
import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sqlalchemy import create_engine
import schedule
import time


# 평균 계산
def calaver():
    
    try:
        print("cal")
        avlist = []
        result = []
        re = "calaver success"
        
        #mid 최댓값, 최소값
        midMx = Movieinfo.objects.aggregate(mid=Max('mid'))
        midmx = Movieinfo.objects.aggregate(mid=Min('mid'))
        
        
        for i in range(midmx['mid'], midMx['mid']+1):
            
            #mid = i 인 영화의 러닝타임
            runti = Movieinfo.objects.filter(mid = i).aggregate(runningtime = Max('runningtime'))
            

            #Data 존재 Check
            datacheck = Bpmdata.objects.filter(mid = i).values_list('bpm', flat=True)

            #최소 10명이 시청 했을 시 분석 시작
            if(len(datacheck) > 10):
                
                #mid = i 인 전체 데이터 호출
                result = Bpmdata.objects.filter(mid = i).values('bpm')
                pnumb = len(result)
                #slist라는 2차원 배열 선언 (행은 측정자 수, 열은 영화 상영시간)
                slist = [[0 for col in range(runti['runningtime'])] for row in range(pnumb)]
                
                #slist라는 2차원 배열에 mid = i인 영화의 개인의 bpm 저장
                for j in range(0, pnumb):

                    slist.insert(j , result[j]['bpm'].split(','))
                
                #sumval 변수에 각 초당 심박수 저장 후 avlist 평균으로 저장하여 db에 insert
                for k in range(0, runti['runningtime']):

                    sumval = 0
                    
                    for l in range(0, pnumb):

                        sumval += int(slist[l][k])
                    
                    avlist.insert(k, sumval / pnumb)
                
                #평균 수치 전부 삭제 후 새로이 저장
                m = Moviegraph.objects.filter(mid=i).all()
                m.delete()

                for j in range(0, len(avlist)):

                    mi = Moviegraph(mid = Movieinfo.objects.get(mid=i), bpm = avlist[j])
                    mi.save()
                print("done")
        return re

    except Exception as e:
        print(e)

# 클러스터링
def cluster():
    
    try:
        
        engine = create_engine('mysql+pymysql://root:bpmservice@27.96.130.250/bpm', convert_unicode = True)
        conn = engine.connect()
        re = "cluster success"

        #mid 최댓값, 최소값
        midMx = Movieinfo.objects.aggregate(mid=Max('mid'))
        midmx = Movieinfo.objects.aggregate(mid=Min('mid'))

        for i in range(midmx['mid'], midMx['mid']+1):
            
            
            #mid = i 인 영화의 러닝타임
            runti = Movieinfo.objects.filter(mid = i).aggregate(runningtime = Max('runningtime'))

            #점수 계산용 변수
            score = 0

            #mid = i 인 영화의 사람 수
            pcount = Bpmtest.objects.filter(mid = i).values_list('tid')
            pnumb = len(pcount)

            #BPMDATA 테이블 전체 호출
            fdata = pd.read_sql_table('BPMDATA', conn)

            #MID = i인 조건부 데이터 전처리
            mdata = fdata[(fdata['MID'] == i)]
            bpmsplit = mdata["BPM"].str.split(',')
            
            print("split")
        
            InsBpmList = [[0 for col in range(runti['runningtime'])] for row in range(pnumb)]
            AvList = [0 for row in range(pnumb)]
            

            for t in range(0, pnumb):
                sumvar = 0
                for y in range(0, runti['runningtime']):
                    
                    InsBpmList[t][y] = int(bpmsplit[t][y])

                    sumvar += InsBpmList[t][y]

                AvList[t] = sumvar / pnumb

            
            fixdata = pd.DataFrame(AvList, columns=['bpm'])
            
            print(fixdata.head)
            points = fixdata.values
            kmeans= KMeans(n_clusters=3)
            kmeans.fit(points)
            kmeans.cluster_centers_
            kmeans.labels_
            fixdata['cluster'] = kmeans.labels_
            
            print(kmeans.cluster_centers_)
            CentA = int(kmeans.cluster_centers_[0])
            CentB = int(kmeans.cluster_centers_[1])
            CentC = int(kmeans.cluster_centers_[2])

            for p in range(0, pnumb):

                dA = int(bpmsplit[p][0]) - CentA
                dB = int(bpmsplit[p][0]) - CentB
                dC = int(bpmsplit[p][0]) - CentC

                disList = [ dA, dB, dC]
                NearData = min(disList)

                if NearData == dA:

                    for a in range(0, runti['runningtime']):
                        if int(bpmsplit[p][a]) > 1.2 * CentA:
                            score += 1
                elif NearData == dB:

                    for a in range(0, runti['runningtime']):
                        if int(bpmsplit[p][a]) > 1.2 * CentB:
                            score += 1
                elif NearData == dC:

                    for a in range(0, runti['runningtime']):
                        if int(bpmsplit[p][a]) > 1.2 * CentC:
                            score += 1

            rpoint = score / pnumb
            
            mi = Scoring.objects.get(mid = i)
            mi.score = rpoint
            mi.save()

            print("done")
    except Exception as e:
        print(e)

    return re

# BPM 최댓값, 최솟값
def Mdata():


    try:

        re = "Mdata Success"
        
        #mid 최댓값, 최소값
        midMx = Movieinfo.objects.aggregate(mid=Max('mid'))
        midmx = Movieinfo.objects.aggregate(mid=Min('mid'))

        
        for i in range(midmx['mid'], midMx['mid']+1):
            
            datacheck = Bpmdata.objects.filter(mid = i).values_list('bpm', flat=True)

            #datacheck 의 길이를 통해 DB에 bpm 데이터가 존재할 경우 실행.
            if(len(datacheck) > 0):

                #mid = i 인 영화의 러닝타임
                runti = Movieinfo.objects.filter(mid = i).aggregate(runningtime = Max('runningtime'))
                
                #mid = i 인 영화의 bpm 데이터
                rdata = Bpmdata.objects.filter(mid = i).values('bpm')
                pnumb = len(rdata)

                # 행 = 측정자 수, 열 = 상영시간 을 가지는 2차원 배열 초기화
                flist = [[0 for col in range(runti['runningtime'])] for row in range(pnumb)]

                # 값 저장용 1차원 배열
                singdlist = []

                # 2차원 배열에 bpm 정보를 전부 split해서 저장
                for j in range(0, pnumb):
            
                    flist.insert(j , rdata[j]['bpm'].split(','))

                # 생성된 2차원 배열 값을 1차원 배열에 전부 저장
                for k in range(0, pnumb):
                    for l in range(0, runti['runningtime']):
                        singdlist.append(int(flist[k][l]))
                
                # max, min method 통해 1차원 배열에서 최댓값, 최솟값 산출
                MaxVal = max(singdlist)
                MinVal = min(singdlist)
                
                # Model orm을 통해 db에 최댓값, 최솟값 저장
                mi = Movieinfo.objects.get(mid = i)
                mi.bmax = MaxVal
                mi.bmin = MinVal
                mi.save()

                print("done")
    except Exception as e:
        print(e)

    return re

# Score에 따른 랭킹 지정
def rating():
    try:
        
        re = "rating success"
        # Scoring에 존재하는 데이터만 랭킹 지정
        ScoreList = Scoring.objects.order_by('mid').all().values_list('score', flat=True)
        MidList = Scoring.objects.order_by('mid').all().values_list('mid', flat=True)
        DataList = [[0 for col in range(2)] for row in range(len(MidList))] 

        
        # mid에 해당하는 score를 가진 DataList 생성
        for p in range(0, len(ScoreList)):
            DataList[p] = [int(MidList[p]), int(ScoreList[p])]
        
        # score를 기준으로 정렬
        DataList = sorted(DataList, key = lambda x: -x[1])

        # 기존의 랭킹 데이터 삭제
        m = Movierank.objects.all()
        m.delete()

        # 순위에 맞게 db 삽입
        for i in range(0, len(MidList)):

            mi = Movierank(mid = Movieinfo.objects.get(mid = DataList[i][0]) , rank = i+1)
            mi.save()
        
        
    except Exception as e:
        print(e)
    
    return re

# schedule.every().day.at("00:00").do(Mdata)
# schedule.every().day.at("01:00").do(calaver)
# schedule.every().day.at("02:00").do(cluster)
# schedule.every().day.at("09:00").do(rating)

# while True:
#     schedule.run_pending()
#     time.sleep(1)