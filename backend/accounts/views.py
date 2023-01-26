from rest_framework import generics
from django.http import JsonResponse

from rest_framework import permissions

from .serializers import RegisterSerializer, LoginSerializer
from .serializers import UserSerializer
from .models import User

# Create your views here.


class SignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = User


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        access = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        return JsonResponse({
            'user': UserSerializer(user).data,
            'access': access,
            'refresh': refresh
        })
