FROM python:3.5
RUN pip3 install django
WORKDIR /usr/src/app
COPY . .
WORKDIR ./BpmService
CMD ["python", "manage.py", "runserver"]
