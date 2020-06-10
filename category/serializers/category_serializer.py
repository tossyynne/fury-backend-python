from rest_framework import serializers
from category.models import Category
from django.utils import timezone

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"