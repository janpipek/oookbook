from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.core.urlresolvers import reverse

from oookbook.models import Book, Loan, LoanLog

@login_required
def new(request):
    book_id = request.REQUEST.get("book_id", None)
    book = get_object_or_404(Book, pk=book_id)
    loan = Loan(book = book, user= request.user, status = Loan.Status.REQUESTED )

    return render(request, 'loans/new.html', {
        'book' : book,
        'loan' : loan,
    })

def index(request):
    if request.method == 'GET':

        loans = Loan.objects.filter(user_id = request.user.id)
        return render(request, 'loans/index.html', {
            'loans' : loans
        })
    else:
        book_id = request.REQUEST.get("book_id", None)
        book = get_object_or_404(Book, pk=book_id)
        loan = Loan(book = book, user = request.user, status = Loan.Status.REQUESTED )
        loan.save()
        try:
            loan.log()
        except:
            loan.delete()
            raise
        # Create a new Loan
        return HttpResponseRedirect(reverse('loans.show', args=[loan.pk]))

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loans/show.html'

    def get_context_data(self, **kwargs):
        context = super(LoanDetailView, self).get_context_data(**kwargs)
        return context