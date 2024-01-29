"""
URL configuration for CookBook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.urls import re_path as url
from backend.views import *

from rest_framework import routers

router = routers.DefaultRouter()

router.get_api_root_view().cls.__name__ = "Api for Cook Book"
router.get_api_root_view().cls.__doc__ = "Простенькое Api для учебного примера"
router.register(r'api/category', CategoryApi)
router.register(r'api/recipe', RecipeApi)
router.register(r'api/category/(?P<id>\d+)/recipe', RecipeApiList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/<int:idd>', RecipeView.as_view(), name='recipe'),
    path('category/<int:id>/recipe/', RecipiesList.as_view(), name='recipies'),
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('category/', CategoryList.as_view(), name='categories'),
    path('', include(router.urls)),
    #url(r'^api/', include((router.urls, 'categories'), namespace='instance_name')),
]
