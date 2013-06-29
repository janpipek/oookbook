from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

# Import all modules to be exported
import books
import users

from oookbook.models import Book
from django.contrib.auth.models import User

def index(request):
    context = {}
    context["user_count"] = User.objects.count()
    context["book_count"] = Book.objects.count()
    return render(request, 'index.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
    context = {}
    return render(request, 'welcome.html', context)