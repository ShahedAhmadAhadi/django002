from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from .models import worker

# Create your views here.

def worker_view(request):
    workers = worker.objects.all()
    context ={
        'workers': workers
    }

    return render(request, './staff/index.html', context)
    
