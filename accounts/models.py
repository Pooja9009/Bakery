from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    profile_pic = models.FileField(upload_to='static/profile', default='static/default_user.jpg')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

