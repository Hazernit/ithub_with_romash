from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Intelligence(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    telephone = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    isWorking = models.BooleanField(False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
