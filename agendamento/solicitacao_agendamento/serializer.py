from rest_framework import  serializers
from .models import Comunicado

class ComunicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicado
        fields = '__all__'
