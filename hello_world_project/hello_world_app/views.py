from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_function(request):
    return HttpResponse('Hello')
