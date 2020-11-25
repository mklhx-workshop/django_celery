FROM python:3.8-buster

WORKDIR /django_celery/

ARG APP_TITLE
ARG DEBUG
ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_PORT
ARG SECRET_KEY

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip -q install --upgrade pip

COPY ./django_app/ /django_celery/

RUN pip -q install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE $DJANGO_PORT

CMD ["bash", "bin/django-start"]
