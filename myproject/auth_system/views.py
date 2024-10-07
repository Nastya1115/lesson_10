from django.shortcuts import render, redirect
from auth_system.forms import UserForm, UserAuthForm
from django.contrib.auth import login, authenticate
from auth_system.models import *
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserForm()

    return render(
        request,
        template_name = 'register.html',
        context = {'form': form}
    )

def login_user(request):
    if request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, 'invalid login or password')
    else:
        form = UserAuthForm()

    return render(
        request,
        template_name = 'login.html',
        context = {'form': form}
    )

def main_page(request):
    if request.user.is_authenticated:
        user = request.user

        if request.method == "POST":
            author = user
            title = request.POST.get("title-field")
            text = request.POST.get("text-field")

            Review.objects.create(title=title, content=text, author=author)

    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(
        request,
        template_name="main.html",
        context=context
    )