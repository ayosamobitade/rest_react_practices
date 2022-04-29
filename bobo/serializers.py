from .models import boboso
from rest_framework import serializers

class boboSerializer(serializers.ModelSerializer):
    class Meta:
        model = boboso
        fields = "__all__"

