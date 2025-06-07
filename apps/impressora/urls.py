
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'impressoras'

router = routers.DefaultRouter()
router.register('', views.ProductViewSet, basename='impressoras')

urlpatterns = [
    path('', include(router.urls) )
]