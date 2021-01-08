from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from . import forms
from main import models
def register(request):
    loginform = UserCreationForm()
    if request.method == "POST":
        loginform = UserCreationForm(request.POST)
        #if loginform.is_valid():
            #username=loginform.cleaned_data['username']
            #password=loginform.cleaned_data['password1']
            #user = authenticate(username = username,password = password,request= request)
            #if user:
                #HttpResponseRedirect('/')
            #else:
                #pass
        if loginform.is_valid():
            loginform.save()
            username=loginform.cleaned_data['username']
            author_data1 = {
                "name": username
                }
            models.Author.objects.create(**author_data1)
                
            return HttpResponseRedirect('/')
    context ={
        "forms" : loginform 
           }
    return render(request,'auth/register.html',context)

def login(request):
        loginForm =forms.LoginForm()
        if request.method == "POST":
            loginform = forms.LoginForm(request.POST)
            if loginform.is_valid():
                username=loginform.cleaned_data['username']
                password=loginform.cleaned_data['password']
                user = authenticate(username = username,password = password)
                if user:
                    auth_login(request, user)
                    print('logged in')
                    return redirect('/')
                else:
                    print('invalid credentials')
        context ={
            "forms1" : loginForm 
            }
        return render(request,'auth/login.html',context)

