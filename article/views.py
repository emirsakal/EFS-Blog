from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse,redirect
from .forms import ArticleForm
from django.contrib import messages

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
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Blog is succesfully created.")
        return redirect("index")
    
    return render(request,"addblog.html",{"form":form})