from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

# http://www.turnkeylinux.org/blog/django-profile
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Book(models.Model):
    title = models.CharField(_("title"), max_length=100)
    author = models.CharField(_("author"), max_length=200)
    note = models.TextField(_("note"), blank=True, null=True)
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
        WITHDRAWN = 6

        STRINGS = (
            "Requested",
            "Approved",
            "Rejected",
            "Borrowed",
            "Returned",
            "Lost",
            "Withdrawn",
        )

        @classmethod
        def to_str(cls, status):
            return cls.STRINGS[status]

        @classmethod
        def owner_allowed(cls, original, new):
            if original == cls.REQUESTED:
                return new in [ cls.APPROVED, cls.REJECTED ]
            elif original == cls.REJECTED:
                return new in [ cls.APPROVED ]
            elif original == cls.BORROWED:
                return new in [ cls.RETURNED, cls.LOST ]
            return False

        @classmethod
        def borrower_allowed(cls, original, new):
            if original == cls.REQUESTED:
                return new in [ cls.WITHDRAWN ]
            elif original == cls.APPROVED:
                return new in [ cls.WITHDRAWN, cls.BORROWED ]
            elif original == cls.BORROWED:
                return new in [ cls.LOST ]
            return False

    class StatusChangeRejected(Exception):
        pass

    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    status = models.IntegerField() # TODO: Limit to choices in Status

    def __unicode__(self):
        return u"Loan of {} ({})".format(self.book, self.Status.to_str(self.status))

    def log(self):
        log = LoanLog(loan = self, user = self.user, status = self.status)
        log.save()  

    def change_status(self, new_status, user):
        if user == self.user:
            if not self.Status.borrower_allowed(self.status, new_status):
                raise Loan.StatusChangeRejected()
        elif user == self.book.user:
            if not self.Status.owner_allowed(self.status, new_status):
                raise Loan.StatusChangeRejected()
        self.status = new_status
        self.log()
        self.save()

    def _get_status_string(self):
        return Loan.Status.to_str(self.status)

class LoanLog(models.Model):
    loan = models.ForeignKey(Loan, db_index = True)
    user = models.ForeignKey(User, db_index = True)
    status = models.IntegerField()
    updated_at = models.DateTimeField(db_index = True)