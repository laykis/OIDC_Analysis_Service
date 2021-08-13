FROM python:3.7
RUN pip3 install --upgrade pip
RUN pip3 install django pymysql scipy pandas seaborn sklearn matplotlib sqlalchemy schedule
RUN pip3 install h5py==2.10.0 --force-reinstall
WORKDIR /usr/src/app
COPY . .
WORKDIR ./BpmService/Bpmrate
CMD ["python", "manage.py", "runserver", "0:8000"]
