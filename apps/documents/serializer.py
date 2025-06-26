from .models import Documents
from rest_framework import serializers

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
        