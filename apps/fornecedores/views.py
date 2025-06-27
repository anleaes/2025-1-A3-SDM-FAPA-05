from django.shortcuts import render
from rest_framework import viewsets
from .models import Fornecedor
from .serializer import FornecedorSerializer
# Create your views here.

<<<<<<< HEAD
from .models import Fornecedor
from rest_framework import viewsets
from .serializer import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
=======
class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
>>>>>>> main
