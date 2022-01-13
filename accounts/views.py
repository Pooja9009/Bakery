from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, ProfileForm
from .forms import CreateUserForm
from cakes.models import Cake, Cart, Wishlist
from .auth import unauthenticated_user, admin_only, user_only
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


def homepage(request):
    cakes = Cake.objects.all().order_by('-id')[:8]
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        items_count = items.count()
        wishlist_items = Wishlist.objects.filter(user=user)
        wishlist_items_count = wishlist_items.count()
        context = {
            'activate_homepage':'active',
            'cakes':cakes,
            'items_count': items_count,
            'wishlist_items_count': wishlist_items_count
        }
        return render(request, 'accounts/homepage.html', context)
    else:
        cakes = Cake.objects.all().order_by('-id')[:8]
        context = {
            'cakes': cakes,
            'activate_homepage': 'active',
        }
        return render(request, 'accounts/homepage.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('/admins')
                elif not user.is_staff:
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid User Credentials")
                return render(request, 'accounts/login.html', {'form_login':form})
    context={
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html',context)

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)

            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to register user')
            return render(request, 'accounts/register.html', {'form_register': form})
    context={
        'form_register': CreateUserForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/register.html',context)

@login_required
@user_only
def profile(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    items_count = items.count()
    profile = request.user.profile
    wishlist_items = Wishlist.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/profile')
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active',
        'items_count': items_count,
        'wishlist_items_count': wishlist_items_count
    }
    return render(request, 'accounts/profile.html', context)

@login_required
@user_only
def change_password(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    items_count = items.count()
    wishlist_items = Wishlist.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Password changed successfully')
            return redirect('accounts/profile.html')
        else:
            messages.add_message(request, messages.ERROR, 'Please verify the form fields')
            return render(request, 'accounts/password_change.html', {'password_change_form':form})
    context = {
        'password_change_form': PasswordChangeForm(request.user),
        'items_count': items_count,
        'activate_profile': 'active',
        'wishlist_items_count': wishlist_items_count
    }
    return render(request, 'accounts/password_change.html', context)



