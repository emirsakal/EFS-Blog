from http.client import HTTP_PORT
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import article

from article.models import Article
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def articles(request):
    articles = Article.objects.all()

    return render(request,"blogs.html",{"articles":articles})

def index(request):
    context = {
        "numbers" :[1,2,3,4,5,6]
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)

        article.author = request.user
        article.save()

        messages.success(request,"Blog is succesfully created.")
        return redirect("article:dashboard")
    
    return render(request,"addblog.html",{"form":form})

def detail(request,id):
    article = get_object_or_404(Article,id = id)
    # article = Article.objects.filter(id = id).first()
    return render(request,"detail.html",{"article":article})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)

    if article.author == request.user:
        if form.is_valid():
            article = form.save(commit = False)
            article.author = request.user
            article.save()

            messages.success(request,"Blog is succesfully updated.")
            return redirect("article:dashboard")
    else:
        messages.info(request,"You don't have permission to update this blog or it doesn't exist.")
        return redirect("article:dashboard")

    
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)

    if article.author == request.user: 
        article.delete()
        messages.success(request, "Blog is succesfully deleted.")  
        return redirect("article:dashboard")
    else:
        messages.info(request,"You don't have permission to delete this blog or it doesn't exist.")
        return redirect("article:dashboard")