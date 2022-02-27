from django.http import HttpResponse
from django.shortcuts import render
from .task import test_celery

# Create your views here.
def test(request):
    test_celery.delay()
    return HttpResponse("Done")
