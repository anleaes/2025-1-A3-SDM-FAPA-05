from .models import Tipos
from rest_framework import serializers

class TiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'