from django.shortcuts import render
from .models import Printer
from rest_framework import viewsets
from .serializer import PrinterSerializer
# Create your views here.

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer  