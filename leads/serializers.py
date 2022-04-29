from .models import lead
from rest_framework import serializers

class leadSerializer(serializers.ModelSerializer):
    class Meta:
        model = lead
        fields = "__all__"
