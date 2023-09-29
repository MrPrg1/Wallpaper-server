from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import *


class WallpaperView(viewsets.ModelViewSet):
    queryset = WallpaperModel.objects.all()
    serializer_class = WallpaperSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer