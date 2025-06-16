from django.shortcuts import render

# Create your views here.
from .models import Tipo
from rest_framework import viewsets
from .serializer import TipoSerializer


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer  