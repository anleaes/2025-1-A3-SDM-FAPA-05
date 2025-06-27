
from .models import RentalOrder
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalOrder
        fields = '__all__'