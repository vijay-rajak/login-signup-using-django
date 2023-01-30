
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        myuser =  User.objects.create_user(username, email, password)

        myuser.save()

        messages.success(request, "Your account has been succrsfully created!")
        return redirect('login')
    else:

        return render(request,'Signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = user.authenticate(email=request.POST.get('email'),
                                         password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            username = user.username
            return render(request,'home.html',{'username': username})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('login')

    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

