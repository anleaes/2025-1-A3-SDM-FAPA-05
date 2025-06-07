from django.shortcuts import render

from .models import Impressora
from rest_framework import viewsets
from .serializer import ImpressoraSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ImpressoraViewSet(viewsets.ModelViewSet):
    queryset = Impressora.objects.all()
    serializer_class = ImpressoraSerializer  