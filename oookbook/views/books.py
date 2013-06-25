from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from oookbook.models import Book

def index(request):
    books = Book.objects.all().order_by('title')[:5]
    context = {'books' : books}
    return render(request, 'books/index.html', context)

def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book' : book}
    return render(request, 'books/show.html', context)
