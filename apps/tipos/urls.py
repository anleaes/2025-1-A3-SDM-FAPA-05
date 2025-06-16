
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tipos'

router = routers.DefaultRouter()
router.register('', views.TipoViewSet, basename='tipos')

urlpatterns = [
    path('', include(router.urls) )
]


path('tipos/', include('tipos.urls', namespace='tipos')),


from django.urls import path, include
