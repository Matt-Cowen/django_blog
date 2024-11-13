from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_1(response):
    return HttpResponse("Hello, Blog!")