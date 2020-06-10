
from rest_framework import viewsets
from category.serializers.category_serializer import CategoryCreateSerializer

from category.models import Category

class CategoryCreateQuery(viewsets.ModelViewSet):
    """ This view implements create category  """
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer