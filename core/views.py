from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerialiser

class HomeView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

