from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u"{}: {}".format(self.author, self.title)
    