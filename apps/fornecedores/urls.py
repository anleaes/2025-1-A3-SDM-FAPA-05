
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'fornecedores'

router = routers.DefaultRouter()
router.register('', views.FornecedorViewSet, basename='fornecedores')

urlpatterns = [
    path('', include(router.urls))
]
