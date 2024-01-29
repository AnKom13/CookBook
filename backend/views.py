from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Recipe
from .serializer import CategoriesListSerializer, CategoryViewSerializer, RecipeViewSerializer, RecipeListSerializer
#from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

#-api
class CategoryApi(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer

class RecipeApiList(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    
    def get_queryset(self):
         queryset = super().get_queryset()
         queryset = Recipe.objects.filter(category=self.kwargs.get('id'))
         return queryset    

class RecipeApi(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    
#---
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryViewSerializer    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Category.objects.filter(id=self.kwargs.get('id'))
        return queryset    


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer


class RecipeView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeViewSerializer    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Recipe.objects.filter(id=self.kwargs.get('idd'))
        return queryset

class RecipiesList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Recipe.objects.filter(category=self.kwargs.get('id'))
        return queryset
 
