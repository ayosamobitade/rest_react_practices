from leads.models import lead
from rest_framework import viewsets, permissions
from .serializers import leadSerializer

class leadViewSet(viewsets.ModelViewSet):
    queryset = lead.objects.all()
    permission_class = [permissions.AllowAny]
    serializer_class = leadSerializer