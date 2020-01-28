from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserSignInForm, UserSignUpForm


def signin_view(request):
    next = request.GET.get('next')
    form = UserSignInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        request.session['user_id'] = user.id
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {'form': form, }
    return render(request, 'signin.html', context)


def signup_view(request):
    next = request.GET.get('next')
    form = UserSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/accounts/login')

    context = {'form': form, }
    return render(request, 'signup.html', context)


def signout_view(request):
    try:
        logout(request)
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/')
