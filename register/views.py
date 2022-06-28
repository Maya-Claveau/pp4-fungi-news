from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def register(response):
    """
    handle the user registration process
    """
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})


def login_user(response):
    """
    handle the user login process
    """
    if response.method == "POST":
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('/')
        else:
            messages.success(response, (
                'There was an error logging in, please try again...'
            ))
            return redirect('login')
    else:
        return render(response, 'authenticate/login.html', {})


def logout_user(response):
    """
    handle the user logout process
    """
    logout(messages.success(response, ('You were logged out.')))
    return redirect('/')
