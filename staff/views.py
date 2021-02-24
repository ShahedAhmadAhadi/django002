from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from .models import worker

# Create your views here.

def worker_view(request):
    workers = worker.objects.all()
    context ={
        'workers': workers,
    }

    return render(request, './staff/index.html', context)

def detail(request, w_id):
    worker_detail = worker.objects.get(pk=w_id)
    context = {
        'detail': worker_detail,
    }
    return render(request, './staff/index.html', context)

    
