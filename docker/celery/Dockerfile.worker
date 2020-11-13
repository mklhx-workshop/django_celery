FROM python:3.8

WORKDIR /django_celery/

COPY ./requirements.txt /django_celery/requirements.txt
RUN pip install -r requirements.txt

COPY . /django_celery/
