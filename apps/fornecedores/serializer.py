
from .models import Fornecedor
from rest_framework import serializers

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'