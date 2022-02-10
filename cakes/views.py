from django.shortcuts import render, redirect
from .forms import CategoryForm, CakeForm, SellerForm, MessageForm, OrderForm, OrderForms
from django.contrib import messages
from .models import Category, Cake, Cart, Seller, MessageUpload, Wishlist, Order
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os
from .filter import CakeFilters
from .models import MessageUpload
from django.core.mail import send_mail


@login_required
@admin_only
# function to add category in category form
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect('/cakes/get_category')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add category')
            return render(request, 'cakes/category_form.html', {'form_category':form})
    context ={
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'cakes/category_form.html', context)

@login_required
@admin_only
# function to get all added category
def get_category(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_category': 'active'
    }
    return render(request, 'cakes/get_category.html', context)

@login_required
@admin_only
# function to delete category
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted successfully')
    return redirect('/cakes/get_category')

@login_required
@admin_only
# function to update category
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect('/cakes/get_category')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update category')
            return render(request, 'cakes/update_category.html', {'form_category':form})
    context ={
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'cakes/update_category.html', context)


@login_required
@admin_only
# function to add cake in form
def cake_form(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cake added successfully')
            return redirect('/cakes/get_cake')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add cake')
            return render(request, 'cakes/cake_form.html', {'form_cake':form})
    context ={
        'form_cake': CakeForm,
        'activate_cake': 'active'
    }
    return render(request, 'cakes/cake_form.html', context)


@login_required
@admin_only
# function to get all added cake
def get_cake(request):
    cakes = Cake.objects.all().order_by('-id')
    cake_filter = CakeFilters(request.GET, queryset=cakes)
    cake_final = cake_filter.qs
    context = {
        'cakes': cake_final,
        'activate_cake': 'active',
        'cake_filter': cake_filter
    }
    return render(request, 'cakes/get_cake.html', context)

@login_required
@admin_only
# function to delete category
def delete_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    os.remove(cake.cake_image.path)
    cake.delete()
    messages.add_message(request, messages.SUCCESS, 'Cake Deleted successfully')
    return redirect('/cakes/get_cake')

@login_required
@admin_only
# function to update category
def update_cake(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    if request.method == "POST":
        if request.FILES.get('cake_image'):
            os.remove(cake.cake_image.path)
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cake updated successfully')
            return redirect('/cakes/get_cake')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update cake')
            return render(request, 'cakes/update_cake.html', {'form_cake':form})
    context ={
        'form_cake': CakeForm(instance=cake),
        'activate_cake': 'active'
    }
    return render(request, 'cakes/update_cake.html', context)

def seller_form(request):
    if request.method == "POST":
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cake added successfully')
            return redirect('/cakes/get_seller')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add cake')
            return render(request, 'cakes/seller_form.html', {'form_seller':form})
    context ={
        'form_seller': SellerForm,
        'activate_seller': 'active'
    }
    return render(request, 'cakes/seller_form.html', context)


@login_required
@admin_only
# function to get all added cake
def get_seller(request):
    sellers = Seller.objects.all().order_by('-id')
    context = {
        'sellers': sellers,
        'activate_seller': 'active'
    }
    return render(request, 'cakes/get_seller.html', context)

@login_required
@admin_only
# function to delete category
def delete_seller(request, cake_id):
    seller = Seller.objects.get(id=cake_id)
    os.remove(seller.seller_image.path)
    seller.delete()
    messages.add_message(request, messages.SUCCESS, 'Cake Deleted successfully')
    return redirect('/cakes/get_seller')

@login_required
@admin_only
# function to update category
def update_seller(request, cake_id):
    seller = Seller.objects.get(id=cake_id)
    if request.method == "POST":
        if request.FILES.get('seller_image'):
            os.remove(seller.seller_image.path)
        form = SellerForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cake updated successfully')
            return redirect('/cakes/get_seller')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update cake')
            return render(request, 'cakes/update_seller.html', {'form_seller':form})
    context ={
        'form_seller': SellerForm(instance=seller),
        'activate_seller': 'active'
    }
    return render(request, 'cakes/update_seller.html', context)


def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        items_count = items.count()
        wishlist_items = Wishlist.objects.filter(user=user)
        wishlist_items_count = wishlist_items.count()
        context = {
            'items_count': items_count,
            'categories': categories,
            'activate_category': 'active',
            'wishlist_items_count': wishlist_items_count
        }
        return render(request, 'cakes/show_categories.html', context)
    else:

        context = {
            'categories':categories,
            'activate_category': 'active',
        }
        return render(request, 'cakes/show_categories.html', context)
# def show_cakes(request):
#     cakes = Cake.objects.all().order_by('-id')
#     context = {
#         'cakes': cakes
#     }
#     return render(request, 'cakes/show_cakes.html', context)

@login_required
def show_cakes(request, category_id):
    categories = Category.objects.get(id=category_id)
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        items_count = items.count()
        wishlist_items = Wishlist.objects.filter(user=user)
        wishlist_items_count = wishlist_items.count()
        context = {
            'activate_category': 'active',
            'categories': categories,
            'items_count': items_count,
            'wishlist_items_count': wishlist_items_count
        }
        return render(request, 'cakes/show_cakes.html', context)
    else:

        context = {
            'categories':categories,
            'activate_category':'active'
        }
        return render(request, 'cakes/show_cakes.html', context)
# def show_sellers(request):
#     sellers = Seller.objects.all().order_by('-id')
#     context = {
#         'sellers': sellers,
#         'activate_seller': 'active'
#     }
#     return render(request, 'accounts/homepage.html', context)

def about_us(request):
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        items_count = items.count()
        wishlist_items = Wishlist.objects.filter(user=user)
        wishlist_items_count = wishlist_items.count()
        context = {
            'activate_about': 'active',
            'items_count':items_count,
            'wishlist_items_count': wishlist_items_count
        }
        return render(request, 'cakes/about.html', context)
    else:
        context = {
            'activate_about': 'active',
        }
        return render(request, 'cakes/about.html', context)

def contact_us(request):
    context = {
        'activate_contact': 'active',
    }
    return render(request, 'cakes/contact.html', context)


@login_required
@user_only
def add_to_cart(request, cake_id):
    user = request.user
    cake = Cake.objects.get(id=cake_id)
    check_presence = Cart.objects.filter(user=user, cake=cake)
    if check_presence:
        messages.add_message(request, messages.ERROR, 'Cake is already added!!Unable to add again')
        return redirect('/cakes/mycart')
    else:
        cart = Cart.objects.create(cake=cake, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Cakes added to cart successfully')
            return redirect('/cakes/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add to cart')

# def addcart(request, cake_id):
#     user = request.user
#     seller = Seller.objects.get(id=cake_id)
#     check_presence = Cart.objects.filter(user=user, seller=seller)
#     if check_presence:
#         messages.add_message(request, messages.ERROR, 'Cake is already added!!Unable to add again')
#         return redirect('/cakes/mycart')
#     else:
#         cart = Cart.objects.create(seller=seller, user=user)
#         if cart:
#             messages.add_message(request, messages.SUCCESS, 'Cakes added to cart successfully')
#             return redirect('/cakes/mycart')
#         else:
#             messages.add_message(request, messages.ERROR, 'Unable to add to cart')
@login_required
@user_only
def add_to_wishlist(request, cake_id):
    user = request.user
    cake = Cake.objects.get(id=cake_id)
    check_presence = Wishlist.objects.filter(user=user, cake=cake)
    if check_presence:
        messages.add_message(request, messages.ERROR, 'Cake is already added!!Unable to add again')
        return redirect('/cakes/wishlist')
    else:
        cart = Wishlist.objects.create(cake=cake, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Cakes added to wishlist successfully')
            return redirect('/cakes/wishlist')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add to cart')


@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user=user).order_by('-id')
    items_count = items.count()
    wishlist_items = Wishlist.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    context = {
        'items_count': items_count,
        'items': items,
        'activate_mycart': 'active',
        'wishlist_items_count': wishlist_items_count,
    }
    return render(request, 'cakes/mycart.html',context)

@login_required
@user_only
def show_wishlist_items(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user).order_by('-id')
    items = Cart.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    items_count = items.count()
    context = {
        'wishlist_items': wishlist_items,
        'activate_wishlist': 'active',
        'wishlist_items_count': wishlist_items_count,
        'items_count': items_count
    }
    return render(request, 'cakes/wishlist.html',context)

@login_required
@user_only
def remove_cart(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    return redirect('/cakes/mycart')

@login_required
@user_only
def remove_wishlist(request, wishlist_id):
    item = Wishlist.objects.get(id=wishlist_id)
    item.delete()
    return redirect('/cakes/wishlist')

@login_required
@user_only
def contact_form(request):
    if request.user.is_authenticated:
        user = request.user
        items = Cart.objects.filter(user=user)
        items_count = items.count()
        wishlist_items = Wishlist.objects.filter(user=user)
        wishlist_items_count = wishlist_items.count()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        }
        message = '''
                           Name: {} 

                           New Message: {}

                           From: {}
                       '''.format(data['name'], data['message'], data['email'], data['phone'])
        send_mail(data['name'], message, '', ['gem00ini99@gmail.com'])

        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Message sent successfully')
            return redirect('/cakes/contact_us')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to send message')
            return render(request, 'cakes/contact.html', {'form_message':form})

    context ={
        'form_message': MessageForm,
        'activate_contact': 'active',
        'items_count':items_count,
        'wishlist_items_count': wishlist_items_count

    }
    return render(request, 'cakes/contact.html', context)


@login_required
@admin_only
# function to get messages in admin panel
def get_message(request):
    message = MessageUpload.objects.all().order_by('-id')
    context = {
        'message':message,
        'activate_message': 'active',

    }
    return render(request, 'cakes/get_message.html', context)

@login_required
@admin_only
# function to delete message
def delete_message(request, message_id):
    message = MessageUpload.objects.get(id=message_id)
    message.delete()
    messages.add_message(request, messages.SUCCESS, 'Message Deleted successfully')
    return redirect('/cakes/get_message')

@login_required
@user_only
# function to order
def order_form(request, cart_id, cake_id):
    user = request.user
    cart = Cart.objects.get(id=cart_id)
    cake = Cake.objects.get(id=cake_id)
    wishlist_items = Wishlist.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    items = Cart.objects.filter(user=user)
    items_count = items.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = cake.cake_price
            total_price = int(quantity)*int(price)
            contact_no = request.POST.get('contact_no')
            address = request.POST.get('address')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(cake=cake,
                                         user=user,
                                         quantity=quantity,
                                         total_price=total_price,
                                         contact_no=contact_no,
                                         address=address,
                                         status = "Pending",
                                         payment_method=payment_method,
                                         payment_status=False

            )
            if order:
                # messages.add_message(request, messages.SUCCESS, 'Cake ordered successfully!! Your order will arrive soon!')
                # cart.delete()
                context = {
                    'order': order,
                    'cart': cart
                }
                return render(request, 'cakes/esewa_payment.html', context)
                # return redirect('/cakes/my_orders')
        else:
            messages.add_message(request,messages.ERROR, 'Could not place order!Something went wrong')
            return render(request,'cakes/order_form.html',{'order_form':form})

    context = {
        'order_form': OrderForm,
        'wishlist_items_count': wishlist_items_count,
        'items_count': items_count
    }
    return render(request, 'cakes/order_form.html', context)

import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/cakes/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/cakes/mycart')


# @login_required
# @user_only
# def my_order(request):
#     user = request.user
#     items = Order.objects.filter(user=user).order_by('-id')
#     context = {
#         'items':items,
#         'activate_myorders':'active'
#     }
#     return render(request, 'cakes/myorder.html', context)

@login_required
@user_only
# function to display users orders
def my_order(request):
    user = request.user
    orders = Order.objects.filter(user=user,payment_status=True).order_by('-id')

    wishlist_items = Wishlist.objects.filter(user=user)
    wishlist_items_count = wishlist_items.count()
    items = Cart.objects.filter(user=user)
    items_count = items.count()
    context = {
        'items':orders,
        'activate_profile':'active',
        'wishlist_items_count': wishlist_items_count,
        'items_count': items_count

    }
    return render(request, 'cakes/myorder.html', context)

@login_required
@admin_only
# function to display all orders
def get_order(request):
    order = Order.objects.all().order_by('-id')
    context = {
        'order': order,
        'activate_order': 'active'
    }
    return render(request, 'cakes/get_order.html', context)


@login_required
@admin_only
# # function to display all orders
def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":

        form = OrderForms(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Order updated successfully')
            return redirect('/cakes/get_order')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update order')
            return render(request, 'cakes/update_order.html', {'form_order': form})
    context = {
        'form_order': OrderForms(instance=order),
        'activate_seller': 'active'
    }
    return render(request, 'cakes/update_order.html', context)

