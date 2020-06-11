from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    #owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=50,blank=True,null=True)
    done = models.BooleanField()
    #updated = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=50)
    class Meta:
        ordering = ['-id']