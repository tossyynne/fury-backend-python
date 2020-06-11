from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

from task.views import TaskCreate

app_name = "team_fury_category"

router = routers.DefaultRouter()

router.register('task', TaskCreate)


urlpatterns = router.urls
