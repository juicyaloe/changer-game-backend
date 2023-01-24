from django.shortcuts import render
from rest_framework import generics

from .models import WeeklyBest
from .serializers import WeeklyBestSerializer

# Create your views here.
class WeeklyBestList(generics.ListAPIView):
    queryset = WeeklyBest.objects.all()
    serializer_class = WeeklyBestSerializer