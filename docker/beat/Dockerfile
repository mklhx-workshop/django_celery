FROM python:3.8-buster

WORKDIR /django_celery/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY ./django_app/ /django_celery/

RUN pip install -r requirements.txt

CMD ["bash", "bin/celery-beat-start"]
