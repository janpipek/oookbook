from django.shortcuts import get_object_or_404, render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from oookbook.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'note']

@login_required
def index(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('title')[:20]
        context = {'books' : books}
        return render(request, 'books/index.html', context)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit = False)
            book.user = request.user
            book.save()
            return HttpResponseRedirect('/books/')
        else:
            return render(request, 'books/new.html', {
                'form': form,
            })

@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book' : book}
    return render(request, 'books/show.html', context)

@login_required
def new(request):
    context = { "form" : BookForm() }
    return render(request, 'books/new.html', context)
