from rest_framework import serializers
from .models import Category, Recipe


from rest_framework.serializers import ModelSerializer

#---api
# class CategoriesApiSerializer(ModelSerializer):

#     recipies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
# #    http_method_names = ['get']
#     class Meta:
#         model = Category
#         fields = "__all__"   

# class RecipeApiSerializer(ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = "__all__"
#---
class CategoryViewSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']      


class CategoriesListSerializer(ModelSerializer):

    recipies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    http_method_names = ['get']
    class Meta:
        model = Category
        fields = ['id','name', 'recipies']   
        
class RecipeViewSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"     
 
class RecipeListSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"
#        depth = 1
        
   

       