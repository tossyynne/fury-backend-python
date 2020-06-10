from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    # date_created = models.DateField(default=timezone.now)
    category_name = models.CharField(max_length=50)
    # task_notes = models.TextField(null=True)
    # task_date = models.DateTimeField()
    
    class Meta:
        ordering = ['-id']


    