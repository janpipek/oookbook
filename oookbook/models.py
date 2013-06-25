from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{}: {}".format(self.author, self.title)
    