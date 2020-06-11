from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    #updated = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=50)
    class Meta:
        ordering = ['-id']