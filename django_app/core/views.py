from django.shortcuts import render
from django_celery.settings import APP_TITLE

# Create your views here.


def index(request):

    return render(
        request,
        "core/index.html",
        {"APP_TITLE": APP_TITLE},
    )
