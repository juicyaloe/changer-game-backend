from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken


# POST only Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[MinLengthValidator(8, '비밀번호를 8자 이상 적어주세요')],
    )

    class Meta:
        model = User
        fields = ('userid', 'password',
                  'name', 'address', 'phone', 'phone_check',
                  'email', 'email_check', 'date_of_birth', 'level')

    def create(self, validated_data):
        temp_phone_check = validated_data['phone_check'] if 'phone_check' in validated_data else False
        temp_email_check = validated_data['email_check'] if 'email_check' in validated_data else False

        user = User.objects.create_user(
            userid=validated_data['userid'],
            name=validated_data['name'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            phone_check=temp_phone_check,
            email=validated_data['email'],
            email_check=temp_email_check,
            date_of_birth=validated_data['date_of_birth'],
            level=validated_data['level'],
        )

        user.set_password(validated_data['password'])
        user.save()

        token = RefreshToken.for_user(user)
        return user


class LoginSerializer(serializers.Serializer):
    userid = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)
            return {
                'user': user,
                'refresh': refresh,
                'access': access
            }
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)