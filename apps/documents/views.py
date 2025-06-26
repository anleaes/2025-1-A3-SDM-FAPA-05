from django.shortcuts import render
from .models import Documents
from rest_framework import viewsets
from .serializer import DocumentsSerializer
# Create your views here.

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer  