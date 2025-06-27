from django.shortcuts import render
from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
