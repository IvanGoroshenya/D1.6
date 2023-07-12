from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'flatpages/default.http')

def index(request):
    return render(request,'flatpages/about.http')