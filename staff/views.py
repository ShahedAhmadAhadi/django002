from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.

def worker_view(request):

    return render(request, './staff/index.html')
    
