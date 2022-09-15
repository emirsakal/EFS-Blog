from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def register(request):
    
    if request.user.is_authenticated:
        messages.info(request,"You can't login more than one account.")
        return redirect("index")

    else:
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            messages.success(request,"You have succesfully registered.")

            return redirect("index")
        context = {
                "form" : form
            }
        return render(request,"register.html",context)


def loginUser(request):
    if request.user.is_authenticated:
        messages.info(request,"You can't login more than one account.")
        return redirect("index")
    
    else:
        form = LoginForm(request.POST or None)
        context = {
            "form" : form
        }

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username,password = password)

            if user is None:
                messages.info(request,"Username or Password is wrong.")
                return render(request,"login.html",context)
            
            messages.success(request,"You successfully logged in.")
            login(request,user)
            return redirect("index")

        return render(request,"login.html",context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You successfully logged out.")
        return redirect("index")
    else:
        messages.info(request,"You can't logout without an acount.")
        return redirect("index")
