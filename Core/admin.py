from django.contrib import admin
from .models import *



@admin.register(WallpaperModel)
class WallpaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'category']
    

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']