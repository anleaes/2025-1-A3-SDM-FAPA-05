
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'documents'

router = routers.DefaultRouter()
router.register('', views.DocumentsViewSet, basename='documentos')

urlpatterns = [
    path('', include(router.urls) )
]