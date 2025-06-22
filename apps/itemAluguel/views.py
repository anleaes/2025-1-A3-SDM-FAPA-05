from django.shortcuts import render
from .models import Itemaluguel
from rest_framework import viewsets
from .serializer import ItemaluguelSerializer
# Create your views here.

class ItemaluguelViewSet(viewsets.ModelViewSet):
    queryset = Itemaluguel.objects.all()
    serializer_class = ItemaluguelSerializer 