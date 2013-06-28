from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

# Import all modules to be exported
import books
import users

def index(request):
    context = {}
    return render(request, 'index.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
    context = {}
    return render(request, 'welcome.html', context)