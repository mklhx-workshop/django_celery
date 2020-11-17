FROM python:3.8

WORKDIR /django_celery/

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN python -m pip install -U pip
# RUN python -m pip install --upgrade pip

COPY ./requirements.txt /django_celery/requirements.txt
RUN pip install -r requirements.txt

COPY . /django_celery/
