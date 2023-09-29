from rest_framework.serializers import ModelSerializer
from .models import *


class WallpaperSerializer(ModelSerializer):
    class Meta:
        model = WallpaperModel
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    category = WallpaperSerializer(read_only=True, many=True)
    class Meta:
        model = CategoryModel
        fields = '__all__'