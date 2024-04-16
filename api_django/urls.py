"""
URL configuration for api_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.api import ProjectViewSet
from projects.views import SendEmailAPI
from projects.viewscorreo import get_email_data

router = DefaultRouter()
router.register('api/projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', SendEmailAPI.as_view(), name='send_email'),
    path('get-email-data/', get_email_data, name='get_email_data'),
    path('', include(router.urls))

]