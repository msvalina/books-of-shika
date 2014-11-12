from django.shortcuts import render, get_list_or_404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from shika.models import Book, BookOwner, LendingRecord, LendingRequest
from shika.forms import BookEntryForm, LendingRequestForm

@login_required
def home(request):
    unconfirmed_requests = LendingRequest.objects.filter(
                           book_owner__name=request.user,
                           is_confirmed=None).count()
    context = {'unconfirmed_requests_num': unconfirmed_requests}
    return render(request, 'shika/home.html', context)

@login_required
def collection(request):
    user = request.user.username
    books = Book.objects.filter(bookowner__name__username=user)

    context = {'books': books}

    return render(request, 'shika/collection.html', context)

def allcollections(request):
    books = Book.objects.all()

    context = {'books': books}

    return render_to_response('shika/collection.html', context,
            context_instance=RequestContext(request))

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
            book_entry = form.save(commit=False)
            book_entry.save()
            book_owner = BookOwner(name=request.user, book=book_entry)
            book_owner.save()
            messages.add_message(request, messages.INFO, 'Book added!')
            return redirect('/shika/bookentry/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookEntryForm()

    return render(request, 'bookentry.html', {'form': form})

@login_required
def lending_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LendingRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            lending_req = form.save(commit=False)
            lending_req.is_sent = True
            lending_req.save()
            messages.add_message(request, messages.INFO, 'Request sent!')
            # redirect to a new URL:
            return redirect('/shika/lending/')

    # if a GET (or any other method) we'll create a blank form with inital value
    # for reader input
    else:
        form = LendingRequestForm(initial={'reader':request.user})

    return render(request, 'lending.html', {'form': form})

@login_required
def confirm_request(request):

    unconfirmed_requests = LendingRequest.objects.filter(
                           book_owner__name=request.user,
                           is_confirmed=None)

    if request.method == 'POST':
        try:
            req_id = request.POST['Confirm']
            req = LendingRequest.objects.get(id=req_id)
            req.is_confirmed = True
            req.save()
            record = LendingRecord(book=req.book, book_owner=req.book_owner,
                    reader=req.reader, request=req)
            record.save()
            messages.add_message(request, messages.INFO, 'Request confirmed!')
            return redirect('/shika/confirm/')
        except KeyError:
            print 'WTf'
        try:
            req_id = request.POST['Deny']
            print req_id
            req = LendingRequest.objects.get(id=req_id)
            req.is_confirmed = False
            req.save()
            messages.add_message(request, messages.INFO, 'Request denyed!')
            return redirect('/shika/confirm/')
        except KeyError:
            print 'WTffff'

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {'requests': unconfirmed_requests}

        return render(request, 'confirmation.html', context)

@login_required
def lending_records(request):
    records = LendingRecord.objects.filter(reader=request.user)

    context = {'records': records}

    return render(request, 'shika/records.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

