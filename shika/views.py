from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'shika/home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

