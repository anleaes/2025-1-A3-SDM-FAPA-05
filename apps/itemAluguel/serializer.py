from .models import Itemaluguel
from rest_framework import serializers

class ItemaluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemaluguel
        fields = '__all__'
        