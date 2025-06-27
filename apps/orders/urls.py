
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'orders'

router = routers.DefaultRouter()
router.register('', views.RentalOrderViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls) )
]