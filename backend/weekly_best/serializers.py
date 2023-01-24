from rest_framework import serializers
from .models import WeeklyBest

class WeeklyBestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'image',
        )
        model = WeeklyBest