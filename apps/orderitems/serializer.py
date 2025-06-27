from .models import RentalItem
from rest_framework import serializers

class RentalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalItem
        fields = '__all__'
