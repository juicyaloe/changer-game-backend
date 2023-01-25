from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

from .serializers import JWTSignupSerializer
from .models import User
# Create your views here.


class JWTSignupView(generics.CreateAPIView):
    serializer_class = JWTSignupSerializer
    queryset = User
