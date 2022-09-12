from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse,redirect

from article.models import Article
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def index(request):
    context = {
        "numbers" :[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

def addarticle(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Blog is succesfully created.")
        return redirect("index")
    
    return render(request,"addblog.html",{"form":form})