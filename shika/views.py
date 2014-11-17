from django.shortcuts import render, get_list_or_404, get_object_or_404
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
    """ Home view presenting number of unconfirmed requests and general info """

    # Query set for unconfirmed requests, observe how query set can filter by
    # other table/model row/attribute bc of foregin key relation
    unconfirmed_requests = LendingRequest.objects.filter(
                           book_owner__name=request.user,
                           is_confirmed=None).count()
    context = {'unconfirmed_requests_num': unconfirmed_requests}

    return render(request, 'shika/home.html', context)

@login_required
def collection(request):
    """ Collection view presenting current users book collection """

    user = request.user.username
    books = Book.objects.filter(bookowner__name__username=user)

    context = {'books': books}

    return render(request, 'shika/collection.html', context)

def allcollections(request):
    """ All collection view presenting all books in model/libraries """

    books = Book.objects.all()

    context = {'books': books}

    # context_instance allows to use request object in template
    return render_to_response('shika/collection.html', context,
            context_instance=RequestContext(request))

@login_required
def book_entry(request):
    """ View for adding books via form and POST method """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookEntryForm(request.POST)
        if form.is_valid():
            # process the data 
            book_entry = form.save(commit=False)
            book_entry.save()
            book_owner = BookOwner(name=request.user, book=book_entry)
            book_owner.save()
            messages.add_message(request, messages.INFO, 'Book added!')
            return redirect('/shika/bookentry/')

    # if a GET (or any other method) create a blank form
    else:
        form = BookEntryForm()

    return render(request, 'bookentry.html', {'form': form})

@login_required
def book_detail(request, book_id):
    """ Detail book view """

    book = Book.objects.get(id=book_id)

    context = {'book': book}

    return render(request, 'shika/bookdetail.html', context)

@login_required
def lending_request(request):
    """ Lending request view """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LendingRequestForm(request.POST)
        if form.is_valid():
            # process the data 
            lending_req = form.save(commit=False)
            lending_req.is_sent = True
            book_owner = BookOwner.objects.get(book=lending_req.book)
            lending_req.book_owner = book_owner
            lending_req.save()
            messages.add_message(request, messages.INFO, 'Request sent to %s!' %
                                 book_owner.name)

            return redirect('/shika/lending/')

    # if a GET (or any other method) create a blank 
    else:
        # Set initial value for LendingRequest form
        form = LendingRequestForm(initial={'reader': request.user})
        # Set query sets for presenting on LendingRequest form fileds 
        # Only show books that are not owned by logged in user
        form.fields['book'].queryset = Book.objects.exclude(
                                       bookowner__name=request.user)
        # Set reader to logged in user
        form.fields['reader'].queryset = User.objects.filter(
                                         username=request.user.username)

    return render(request, 'lending.html', {'form': form})

@login_required
def confirm_request(request):
    """ Confirm request view shows unconfirmed request """

    # Query set for unconfirmed requests, observe how query set can filter by
    # other table/model row/attribute bc of foregin key relation
    unconfirmed_requests = LendingRequest.objects.filter(
                           book_owner__name=request.user,
                           is_confirmed=None)

    if request.method == 'POST':
        try:
            # capture value (req_id) from key Confirm set by POST method
            req_id = request.POST['Confirm']
            # get related lending request
            req = LendingRequest.objects.get(id=req_id)
            # change is_confirmed attribute
            req.is_confirmed = True
            # save object to db
            req.save()
            # create LendingRecord object from saved lending request
            record = LendingRecord(book=req.book, book_owner=req.book_owner,
                     reader=req.reader, request=req)
            # save record to db
            record.save()
            # print message to the user
            messages.add_message(request, messages.INFO, 'Request confirmed!')

            return redirect('/shika/confirm/')

        except KeyError:
            pass
            # print 'WTf'
        try:
            # get value from Deny key set in POST method
            req_id = request.POST['Deny']
            # get related lending request
            req = LendingRequest.objects.get(id=req_id)
            # set is_confirmed to false and save object
            req.is_confirmed = False
            req.save()
            # print message to the user
            messages.add_message(request, messages.INFO, 'Request denied!')

            return redirect('/shika/confirm/')

        except KeyError:
            pass
            # print 'WTffff'

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {'requests': unconfirmed_requests}

        return render(request, 'confirmation.html', context)

@login_required
def lending_records(request):
    """ Lending records view shows current users lended books """

    records = LendingRecord.objects.filter(reader=request.user)

    context = {'records': records}

    return render(request, 'shika/records.html', context)

def logout_view(request):
    """ Logout view called from books_of_shika/urls """
    logout(request)
    return redirect('/')

