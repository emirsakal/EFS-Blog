from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        "numbers" :[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
