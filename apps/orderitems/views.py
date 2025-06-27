from .models import RentalItem
from rest_framework import viewsets
from .serializer import RentalItemSerializer
# Create your views here.

class RentalItemViewSet(viewsets.ModelViewSet):
    queryset = RentalItem.objects.all()
    serializer_class = RentalItemSerializer
