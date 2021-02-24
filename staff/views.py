from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.

def worker_view(request):
    return HttpResponse('<h1>view Working</h1>')
    
