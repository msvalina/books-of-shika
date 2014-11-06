from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    """ Book model """
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_lended = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author + " by " + self.name

class BookOwner(models.Model):
    """ Book owners model """
    name = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return str(self.name) + " - " + str(self.book)

class LendingRequest(models.Model):
    """ Book lending request """
    reader = models.ForeignKey(User)
    book_owner = models.ForeignKey(BookOwner)
    book = models.ForeignKey(Book)
    is_sent = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.id)
    
class LendingRecords(models.Model):
    """ Book lending records model """ 
    book = models.ForeignKey(Book)
    book_owner = models.ForeignKey(BookOwner)
    reader = models.ForeignKey(User)
    request = LendingRequest(LendingRequest)

    def __unicode__(self):
        return str(self.id)
