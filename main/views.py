from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import (
    authenticate, get_user_model, login, logout
)

from .forms import UserLoginForm, UserRegisterForm


class IndexView(generic.ListView):
    template_name = 'main/index.html'

    def get_queryset(self):
        return None


def history(request):
    return render(request, 'main/history.html')


def login_view(request):
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('/')

    return render(request, 'main/form.html', {'form': form, 'title': title})


def register_view(request):
    title = 'Sign in'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect('/')

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'main/form.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')



































