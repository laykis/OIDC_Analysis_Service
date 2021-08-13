FROM python:3.5
RUN pip3 install django
WORKDIR ./BpmService
CMD ["python", "manage.py", "runserver"]
