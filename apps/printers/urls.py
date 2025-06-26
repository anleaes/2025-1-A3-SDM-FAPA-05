
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'printers'

router = routers.DefaultRouter()
router.register('', views.PrinterViewSet, basename='impressoras')

urlpatterns = [
    path('', include(router.urls) )
]
