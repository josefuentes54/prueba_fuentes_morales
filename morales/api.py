from .models import Carreras
from rest_framework import viewsets, permissions
from .serializers import CarrerasSerializers

class CarrerasSerializersViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarrerasSerializers