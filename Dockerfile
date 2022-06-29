# base image
FROM python:3.8

# setup environment variable
#ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir /code

# where your code lives
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt  /code/

# copy whole project to your docker home directory.
COPY .  /code/
# run this command to install all dependencies
# RUN pip install -r requirements.txt
RUN python -m pip install -q --no-cache-dir -r requirements.txt
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py runserver 0.0.0.0:8000 --settings=config.settings.local
