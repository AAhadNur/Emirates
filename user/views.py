from django.shortcuts import render, redirect
from django.contrib import messages

from user.forms import CreateNormalUserForm, CreateSuperUserForm
# Create your views here.


def signup(request):
    return render(request, 'user/signup.html')


def signup_normal_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CreateNormalUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = CreateNormalUserForm()

    context = {'form': form}

    return render(request, 'user/normal_user_signup.html', context)


def signup_super_user(request):
    page = 'admin'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CreateSuperUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully as Admin.')
            return redirect('home')
    else:
        form = CreateSuperUserForm()

    context = {'form': form, 'page': page}

    return render(request, 'user/normal_user_signup.html', context)
