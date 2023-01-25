from rest_framework import serializers
from .models import User

# TODO: 유효성 검사 추가
class JWTSignupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
