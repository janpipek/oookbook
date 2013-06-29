from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from oookbook.models import Book, Loan, LoanLog

@login_required
def borrow(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    loan = Loan(book = book, user= request.user, status = Loan.Status.REQUESTED )
    loan.save()
    try:
        loan.log()
    except:
        loan.delete()
        raise
    return HttpResponseRedirect('/books/')
