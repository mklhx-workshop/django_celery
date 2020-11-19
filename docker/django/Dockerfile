FROM python:3.8-buster

WORKDIR /django_celery/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    avahi-daemon \
    samba

RUN python -m pip install --upgrade pip

COPY ./django_app/ /django_celery/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# RUN bash bin/apply-ssl

CMD ["bash", "bin/start-servers"]
