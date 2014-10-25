from django.db import models

class Book(models.Model):
    """ Book model """
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_lended = models.BoolenField(default=False)

class BookOwner(model.Model):
    """ Book owners model """
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book)

class Reader(models.Model):
    """ Reader model """
    name = models.CharField(max_length=200, null=True, blank=True)
    book = models.ForeignKey(Book)

class LendingRequest(model.Model):
    """ Book lending request """
    reader = models.ForeignKey(Reader)
    book_owner = models.ForeignKey(BookOwner)
    book = models.ForeignKey(Book)
    sent = models.BoolenField(default=False)
    confirmed = models.BoolenField(default=False)
    
class LendingRecords(model.Model):
    """ Book lending records model """ 
    book = models.ForeignKey(Book)
    book_owner = models.ForeignKey(BookOwner)
    reader = models.ForeignKey(Reader)
    request = LendingRequest(LendingRequest)
