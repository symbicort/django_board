from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request,'signup.html', {'signupForm' : signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()

        return redirect('/')

def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request,'login.html', {'loginForm' : loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/')

def logout(request):
    # 세션 정보를 지우는 것
    auth_logout(request)
    return redirect('/')


