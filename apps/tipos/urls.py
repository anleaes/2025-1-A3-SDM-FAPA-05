
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tipos'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='tipos')

urlpatterns = [
    path('', include(router.urls) )
]
