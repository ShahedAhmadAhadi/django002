from django.db import models

# Create your models here.

class worker(models.Model):
    w_name = models.CharField(max_length=32)
    w_field = models.CharField(max_length=32)
    w_phone = models.CharField(max_length=10)
    w_age = models.IntegerField()
    w_email = models.EmailField()
    w_image = models.CharField(max_length=500, default='https://www.google.com/url?sa=i&url=https%3A%2F%2Ftrademark.eu%2Fteam%2Fpintz-associate-placeholder%2F&psig=AOvVaw1np7dteIwQekhimY1hEQKi&ust=1614228112495000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKix2szage8CFQAAAAAdAAAAABAD')
