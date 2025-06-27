from django.shortcuts import render
from .models import Printer
from rest_framework import viewsets
from .serializer import PrinterSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer   
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'date_fabrication', 'is_active', 'category']


# Carregando todos os produtos
#queryset = Product.objects.all()

# Filtrando produtos
#queryset = Product.objects.filter()

# Filtrando e ordenando por categoria decrescente
#queryset = Product.objects.filter().order_by('-category')
