from django.contrib import admin
from shika.models import Book, BookOwner, Reader, LendingRequest, LendingRecords

admin.site.register(Book)
admin.site.register(BookOwner)
admin.site.register(Reader)
admin.site.register(LendingRequest)
admin.site.register(LendingRecords)


