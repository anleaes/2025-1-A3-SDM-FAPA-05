
from .models import Impressora
from rest_framework import serializers

class ImpressoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impressora
        fields = '__all__'