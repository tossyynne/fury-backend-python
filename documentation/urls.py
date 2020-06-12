from rest_framework import routers
from django.urls import path, include
from documentation.views import Documentation_view
app_name= "Documentation"
router = routers.DefaultRouter()
router.register('', Documentation_view)
urlpatterns = router.urls


