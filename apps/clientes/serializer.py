
from .models import Cliente
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'