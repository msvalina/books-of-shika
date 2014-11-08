from django.contrib import admin
from shika.models import Book, BookOwner, LendingRequest, LendingRecord

admin.site.register(Book)
admin.site.register(BookOwner)
admin.site.register(LendingRequest)
admin.site.register(LendingRecord)


