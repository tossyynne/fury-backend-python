from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Documentation(models.Model):
    
    path_name = models.CharField(max_length=500)
    action_name = models.CharField(max_length=500)
    route= models.CharField(max_length=500)
    curl= models.CharField(max_length=500)
    class Meta:
        ordering = ['-id']
    