from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

from category.viewsets.category_viewset import CategoryCreateQuery

app_name = "team_fury_category"

router = routers.DefaultRouter()

router.register('category', CategoryCreateQuery)


urlpatterns = router.urls
