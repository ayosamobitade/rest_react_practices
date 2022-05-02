from rest_framework import serializers
from .models import momo

class momoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = momo
        