from django.urls import path

from . import views

urlpatterns = [
    path('', views.WeeklyBestList.as_view()),
]