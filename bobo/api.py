from .models import boboso
from .serializers import boboSerializer

from rest_framework import viewsets, permissions

class boboViewset(viewsets.ModelViewSet):
    queryset = boboso.objects.all()
    permission_class = [permissions.AllowAny]

    serializer_class = boboSerializer