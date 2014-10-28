from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print "test"
    return HttpResponse("Wooow ulogiran sam")
