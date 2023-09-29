from django.db import models



class WallpaperModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image")
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



