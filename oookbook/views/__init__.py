from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Import all modules to be exported
import books
import users
import loans

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

@login_required
def welcome(request):
    context = {}
    return render(request, 'welcome.html', context)

def register(request):
    context = {}
    if request.method == 'GET':
        context["form"] = UserCreationForm()
        return render(request, 'register.html', context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            context["form"] = UserCreationForm()
            return render(request, 'register.html', context)
