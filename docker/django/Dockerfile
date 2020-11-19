FROM python:3.8-slim-buster

WORKDIR /django_celery/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY . /django_celery/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD ["gunicorn", "django_celery.wsgi:application", "--workers 2", "--timeout 90", "--graceful-timeout 20", "--keep-alive 5", "--max-requests 1000", "--bind 0.0.0.0:8000"]
