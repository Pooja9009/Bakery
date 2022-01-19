from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cakes.models import *
from django.contrib import messages

@login_required
@admin_only
# method to view admin dashboard
def admin_dashboard(request):
    category = Category.objects.all()
    category_count = category.count()
    cake = Cake.objects.all()
    cake_count = cake.count()
    message = MessageUpload.objects.all()
    message_count = message.count()
    order = Order.objects.all()
    order_count= order.count()
    users = User.objects.filter(is_staff=0)
    users_count = users.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()
    context = {
        'category': category_count,
        'cake': cake_count,
        'message': message_count,
        'order': order_count,
        'users': users_count,
        'admin': admin_count
    }
    return render(request, 'admins/admin_dashboard.html', context)



@login_required
@admin_only
def show_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users,
        'activate_users':'active'
    }
    return render(request, 'admins/users.html', context)

@login_required
@admin_only
def show_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins': admins,
        'activate_admins': 'active'
    }
    return render(request, 'admins/admins.html', context)

@login_required
@admin_only
def promote_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/admins')

@login_required
@admin_only
def demote_admin(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.SUCCESS, 'Admin demoted to user')
    return redirect('/admins/users')

@login_required
@admin_only
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/admins/users')
