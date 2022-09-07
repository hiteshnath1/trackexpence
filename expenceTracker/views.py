from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from matplotlib.style import context
from expenceApp.forms import loginForm,signUpForm
from django.contrib import messages
import datetime


def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    error_message = None
    # form = AuthenticationForm()
    date = datetime.datetime.now()
    if date.hour >= 1 and date.hour < 11:
        msg = 'Good Morning'
        mtype = 'success'
    elif date.hour >= 11 and date.hour <= 16:
        msg= 'Good Afternoon'
        mtype = 'danger'

    else:
        msg = 'Good Evening'
        mtype = 'warning'
    form = loginForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,msg)

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('/')
        else:
            error_message='Ups... something went wrong'

    context = {
        'form' : form,
        'error_message':error_message
    }
    return render(request, 'auth/login1.html',context)

def signup(request):
    msg     = None
    success = False
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg     = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'

    else:
        form = signUpForm()
    context = {
        "form":form,
        "msg" : msg, 
        "success" : success 
    }
    
    return render(request, 'auth/signup.html',context)
