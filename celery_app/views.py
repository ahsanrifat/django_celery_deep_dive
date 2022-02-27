from django.http import HttpResponse
from django.shortcuts import render
from .task import test_celery, send_email

# Create your views here.
def test(request):
    send_email.delay()
    return HttpResponse("Done")
