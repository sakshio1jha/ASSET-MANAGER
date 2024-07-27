from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"git.html")

def login(request):
    return render(request,"login.html")

