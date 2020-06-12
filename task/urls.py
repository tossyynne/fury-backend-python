from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

from task.views import TaskCreate

app_name = "task"

router = routers.DefaultRouter()

router.register('', TaskCreate)


urlpatterns = router.urls
