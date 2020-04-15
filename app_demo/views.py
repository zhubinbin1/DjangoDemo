from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("hello world")


def msg(request, name, age):
    return HttpResponse('My name is ' + name + ',i am ' + age + ' years old')
