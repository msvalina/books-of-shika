from django.shortcuts import render, get_list_or_404
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shika.models import Book, BookOwner, LendingRecords, LendingRequest
from shika.forms import BookEntryForm

@login_required
def home(request):
    return render(request, 'shika/home.html')

@login_required
def collection(request):
    user = request.user.username
    books = Book.objects.filter(bookowner__name__username=user)

    context = {'books': books}

    return render(request, 'shika/collection.html', context)

@login_required
def book_entry(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookEntryForm()

    return render(request, 'bookentry.html', {'form': form})

@login_required
def thanks(request):
    return HttpResponse("thanks")

def logout_view(request):
    logout(request)
    return redirect('/')

