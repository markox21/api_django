from django.urls import path
from rest_framework import routers
from projects.api import ProjectViewSet
from projects.views import SendEmailAPI
from projects.viewscantidad import CantidadProductosView

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls + [
    path('send-email/', SendEmailAPI.as_view(), name='send-email'),
    path('get-cantidad-productos/<str:product_name>/', CantidadProductosView.as_view(), name='get_cantidad_productos'),

]
