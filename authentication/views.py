from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from smsgenerator import views as smsgenerator_views

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
            return render(request, 'authentication/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect(smsgenerator_views.home)
            except IntegrityError: 
                return render(request, 'authentication/signupuser.html', {'form':UserCreationForm(), 'error':'User has been taken'})
        else: 
            return render(request, 'authentication/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(smsgenerator_views.home)

def loginuser(request):
    if request.method == 'GET':
            return render(request, 'authentication/signinuser.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/signinuser.html', {'form': AuthenticationForm(), 'error': 'Username and password does not match'})
        else: 
            login(request,user)
            return redirect(smsgenerator_views.home)

            

       

