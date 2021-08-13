# Generated by Django 3.2.5 on 2021-07-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bpmdata',
            fields=[
                ('bid', models.BigAutoField(db_column='BID', primary_key=True, serialize=False)),
                ('tsec', models.IntegerField(db_column='TSEC')),
                ('bpm', models.IntegerField(db_column='BPM')),
            ],
            options={
                'db_table': 'BPMDATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movieinfo',
            fields=[
                ('mid', models.BigAutoField(db_column='MID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=100)),
            ],
            options={
                'db_table': 'MOVIEINFO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movierank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(db_column='RANK')),
            ],
            options={
                'db_table': 'MOVIERANK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('uid', models.BigAutoField(db_column='UID', primary_key=True, serialize=False)),
                ('uname', models.CharField(db_column='UNAME', max_length=50)),
                ('userid', models.CharField(db_column='USERID', max_length=50)),
                ('userpw', models.CharField(db_column='USERPW', max_length=50)),
                ('usex', models.CharField(db_column='USEX', max_length=2)),
                ('useremail', models.CharField(db_column='USEREMAIL', max_length=50)),
                ('unumber', models.CharField(db_column='UNUMBER', max_length=15)),
                ('uage', models.CharField(blank=True, db_column='UAGE', max_length=6, null=True)),
            ],
            options={
                'db_table': 'USERINFO',
                'managed': False,
            },
        ),
    ]
