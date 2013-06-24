from django.shortcuts import render

import books

def index(request):
    context = {}
    return render(request, 'index.html', context)