from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


def Home(request: HttpRequest):
    return HttpResponse('Hello World, This is my new HOME !')
