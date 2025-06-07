from django.shortcuts import render
#git add .
#git commit -m "Enviando info"
#git push origin main
# Create your views here.

from .models import Impressora
from rest_framework import viewsets
from .serializer import ImpressoraSerializer

# Após o comentario "# Create your views here." e crie as views "Product".

class ImpressoraViewSet(viewsets.ModelViewSet):
    queryset = Impressora.objects.all()
    serializer_class = ImpressoraSerializer  