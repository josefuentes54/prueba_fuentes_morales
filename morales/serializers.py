from rest_framework import serializers
from .models import Carreras

class CarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = ('id', 'nombre', 'años', 'asignaturas', 'descripcion')