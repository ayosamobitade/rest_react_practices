from rest_framework import viewsets, permissions
from .serializers import momoSerializers
from .models import momo

class momoViewSets(viewsets.ModelViewSet):
    queryset = momo.objects.all()
    permission_class = [permissions.AllowAny]
    serializer_class = momoSerializers