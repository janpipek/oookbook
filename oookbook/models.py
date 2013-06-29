from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

    def __unicode__(self):
        return u"{}: {}".format(self.author, self.title)

class Loan(models.Model):
    class Status:
        REQUESTED = 0
        APPROVED = 1
        REJECTED = 2
        BORROWED = 3
        RETURNED = 4
        LOST = 5

    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    status = models.IntegerField() # TODO: Limit to choices in Status

class LoanLog(models.Model):
    loan = models.ForeignKey(Loan, db_index = True)
    user_id = models.ForeignKey(User, db_index = True)
    status = models.IntegerField()
    updated_at = models.DateTimeField(db_index = True)