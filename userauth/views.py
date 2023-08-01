from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, RegisterOrganisation, ForgotPasswordForm
from django.contrib.auth.forms import PasswordChangeForm

import random
import string

from .models import CustomUser

from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail

def login_user(request):
    notifications = messages.get_messages(request)
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'notifications': notifications
    }
    return render(request, 'login.html', context)

def forgot_password(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    if request.method == 'POST':
        form = ForgotPasswordForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            if CustomUser.objects.filter(email=email).exists():
                user_account = CustomUser.objects.get(email=email)

                def generate_random_string(length=8):
                    characters = string.ascii_letters + string.digits
                    random_string = ''.join(random.choices(characters, k=length))
                    return random_string
                temp_pass = generate_random_string()

                user_account.set_password(temp_pass)
                user_account.save()

                # Email Notification
                subject = 'CTR: Password Reset'
                message = f"Greetings {user_account.first_name} {user_account.last_name},\nYour Password has been reset.\n\nTemporary Password: {temp_pass}\n\nKindly use this password to reset your password.\n\nRegards\nTeam CTR, ICMR"
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)

                messages.success(request, f'Password instructions for {email} mailed!')
                return redirect('/login')
            else:
                messages.error(request, f'An account with the email id {email} doesnot exist!')
                return redirect('/login')
        else:
            form.add_error(None, 'Invalid username or password.')
    else:
        form = ForgotPasswordForm()

    context = {'form': form}
    return render(request, 'forgotpassword.html', context)

def reset_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password reset successfully!')
            return redirect('/dashboard')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'passwordreset.html', context)

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Email Notification
            subject = 'CTR: New User Registered'
            message = f"A new user has registered:\n\nName: {user.first_name} {user.last_name}\nEmail: {user.email}\n\nPlease take appropriate action."
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]
            send_mail(subject, message, from_email, recipient_list)

            form.save()
            return redirect('/login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def register_organisation(request):
    if request.method == 'POST':
        form = RegisterOrganisation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register')
    else:
        form = RegisterOrganisation()

    context = {'form': form}
    return render(request, 'registerorganisation.html', context)

def logout_user(request):
    logout(request)
    return redirect('dashboard:dashboard')