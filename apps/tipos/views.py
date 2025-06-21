from django.shortcuts import render
from .models import Impressora
from rest_framework import viewsets
from .serializer import ImpressoraSerializer
# Create your views here.

class ImpressoraViewSet(viewsets.ModelViewSet):
    queryset = Impressora.objects.all()
    serializer_class = ImpressoraSerializer  
    