from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=250, null=True, validators=[validators.MinLengthValidator(2)])
    category_description = models.TextField()
    category_image = models.FileField(upload_to='static/uploads', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name


class Cake(models.Model):
    cake_name = models.CharField(max_length=200)
    cake_price = models.FloatField()
    cake_image = models.FileField(upload_to='static/uploads')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)  # (on_delete)if category deleted then food inside category will also be deleted
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cake_name


class Seller(models.Model):
    seller_name = models.CharField(max_length=200)
    seller_price = models.FloatField()
    seller_image = models.FileField(upload_to='static/uploads')
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.seller_name


class Cart(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class MessageUpload(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, validators=[validate_email])
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=200)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
    )
    cake = models.ForeignKey(Cake, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    payment_method = models.CharField(max_length=200, choices=PAYMENT, null=True)
    payment_status = models.BooleanField(default=False, null=True, blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
