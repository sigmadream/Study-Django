from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from authy.forms import SignupForm, ChangePasswordForm


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'change_password.html', context)


def password_change_done(request):
    return render(request, 'change_password_done.html')
