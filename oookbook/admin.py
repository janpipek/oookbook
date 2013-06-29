from django.contrib import admin
from oookbook.models import Book, Loan, LoanLog

admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(LoanLog)

