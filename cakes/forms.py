from django import forms
from django.forms import ModelForm

from .models import Category, Cake, Seller, MessageUpload, Order

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class CakeForm(ModelForm):
    class Meta:
        model = Cake
        fields = "__all__"

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"

class MessageForm(ModelForm):
    class Meta:
        model = MessageUpload
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity','contact_no', 'address']

class OrderForms(ModelForm):
    class Meta:
        model = Order
        fields = ['status']