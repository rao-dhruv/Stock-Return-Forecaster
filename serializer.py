from rest_framework import serializers
from .models import stockmarket


class stockmarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = stockmarket
        fields = "__all__"
