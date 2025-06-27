from django.shortcuts import render
from .models import RentalOrder
from rest_framework import viewsets
from .serializer import OrderSerializer
# Create your views here.

class RentalOrderViewSet(viewsets.ModelViewSet):
    queryset = RentalOrder.objects.all()
    serializer_class = OrderSerializer