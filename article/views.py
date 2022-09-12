from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse
from .forms import ArticleForm

def index(request):
    context = {
        "numbers" :[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")

def addblog(request):
    form = ArticleForm()
    
    return render(request,"addblog.html",{"form":form})