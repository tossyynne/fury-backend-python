"""todo_team_fury URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path as url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from todo_team_fury import settings
from rest_framework_swagger.views import get_swagger_view
#==================================
#DJANGO ADMIN custom
#==================================
admin.site.site_header = "Team Fury To-Do"
admin.site.site_title = "Team Fury To-Do App Portal"
admin.site.index_title = "Welcome to Team Fury To-Do App Portal"

schema_view = get_swagger_view(title='Team-Fury Api Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),

    # This will take you to the different endpoints in tasks
    path('v1/task/', include('task.urls')),
    #this is for account registration
    path('v1/register/', include('account.urls')),
    path('v1/documentation/',include('documentation.urls')),
    # This will show you all the available endpoint in this project
    path('', schema_view),
   
    # more
]


