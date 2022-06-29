from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def register(request):
    """
    handle the user registration process
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


def login_user(request):
    """
    handle the user login process
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('/')
        else:
            messages.success(response, (
                'There was an error logging in, please try again...'
            ))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    """
    handle the user logout process
    """
    logout(messages.success(request, ('You were logged out.')))
    return redirect('/')
