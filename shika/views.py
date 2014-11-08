from django.shortcuts import render, get_list_or_404
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from shika.models import Book, BookOwner, LendingRecord, LendingRequest
from shika.forms import BookEntryForm, LendingRequestForm

@login_required
def home(request):
    return render(request, 'shika/home.html')

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
            form.save()
            return HttpResponseRedirect('thanks/')

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
            # redirect to a new URL:
            return HttpResponseRedirect('thanks/')

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
            print req_id
            req = LendingRequest.objects.get(id=req_id)
            req.is_confirmed = True
            req.save()
            return redirect('/shika/confirm/')
        except KeyError:
            print 'WTf'
        try:
            req_id = request.POST['Deny']
            print req_id
            req = LendingRequest.objects.get(id=req_id)
            req.is_confirmed = False
            req.save()
            return redirect('/shika/confirm/')
        except KeyError:
            print 'WTffff'

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {'requests': unconfirmed_requests}

        return render(request, 'confirmation.html', context)

@login_required
def thanks(request):
    return HttpResponse("thanks")

def logout_view(request):
    logout(request)
    return redirect('/')

