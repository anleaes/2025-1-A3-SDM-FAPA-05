from django.shortcuts import render

# Create your views here.

from .models import Fornecedor
from rest_framework import viewsets
from .serializer import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer