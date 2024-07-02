from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

from .forms import SignupForm, LoginForm

@csrf_exempt
def signup(request):
    if request.method == "GET":
        signupForm = SignupForm()
        return render(request, 'signup.html', {'signupForm': signupForm})
    elif request.method == "POST":
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('/user/login')
        else:
            return render(request, 'signup.html', {'signupForm': signupForm})

@csrf_exempt
def login(request):
    if request.method == "GET":
        loginForm = LoginForm()
        return render(request,'login.html', {'loginForm' : loginForm})
    elif request.method == "POST":
        loginForm = LoginForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/')
        else:
            return render(request, 'login.html', {'loginForm' : loginForm})

def logout(request):
    auth_logout(request)
    return redirect('/')


