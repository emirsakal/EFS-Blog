from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")
