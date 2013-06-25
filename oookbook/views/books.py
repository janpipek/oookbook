from django.shortcuts import get_object_or_404, render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from oookbook.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'note']

def index(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('title')[:20]
        context = {'books' : books}
        return render(request, 'books/index.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit = False)
            book.save()
            return HttpResponseRedirect('/books/')
        else:
            return render(request, 'books/new.html', {
                'form': form,
            })

def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book' : book}
    return render(request, 'books/show.html', context)

def new(request):
    context = { "form" : BookForm() }
    return render(request, 'books/new.html', context)
