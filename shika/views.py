from django.shortcuts import render, get_list_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shika.models import Book, BookOwner, Reader, LendingRecords, LendingRequest

@login_required
def home(request):
    return render(request, 'shika/home.html')

@login_required
def collection(request):
    user = request.user.username
    books = Book.objects.filter(bookowner__name__username=user)

    context = {'books': books}

    return render(request, 'shika/collection.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

