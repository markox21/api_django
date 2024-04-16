from django.urls import path
from rest_framework import routers
from projects.api import ProjectViewSet
from projects.views import SendEmailAPI

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls + [
    path('send-email/', SendEmailAPI.as_view(), name='send-email')
]