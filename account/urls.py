from rest_framework import routers
from django.urls import path, include
from account.views import registration_view


app_name= "account"


router = routers.DefaultRouter()

router.register('register', registration_view)


urlpatterns = router.urls


