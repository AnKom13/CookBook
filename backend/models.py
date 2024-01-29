from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return f"{self.name}"

    
    
class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, related_name="recipies", on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        ordering = ['id']    
        
    def __str__(self):
        return f"{self.name}"    