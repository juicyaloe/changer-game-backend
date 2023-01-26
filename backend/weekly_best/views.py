from django.shortcuts import render
from rest_framework import generics

from rest_framework import permissions

from .models import WeeklyBest
from .serializers import WeeklyBestSerializer

# Create your views here.
class WeeklyBestList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = WeeklyBest.objects.all()
    serializer_class = WeeklyBestSerializer