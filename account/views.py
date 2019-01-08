from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseForbidden
from .forms import UserCreateForm
from django.contrib.auth import authenticate, login


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('success')
        return HttpResponse('wrong_data')
    return HttpResponse('Error method!')

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return HttpResponse('User Created')
        else:
            return HttpResponseForbidden()
    return HttpResponse('This is sign up page')


def errMsg(request):
    return HttpResponse('Method is not found')