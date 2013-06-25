from django.shortcuts import render

# Import all modules to be exported
import books
import users

def index(request):
    context = {}
    return render(request, 'index.html', context)