from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context)
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('/login/')
        else:
            return render(request, 'users/register.html', context={'form': form})


def login_view(request):
    if request.method == 'GET':
        context = {'form': LoginForm}
        return render(request, 'users/login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error('username', 'Username or password is incorrect')

        return render(request=request, template_name='users/login.html', context={'form': form})


def logaut_view(request):
    logout(request)
    return redirect('/products/')


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html', {'user': request.user})
