"""diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path
from exercise.views import exercise_api, exercise_diet_admin_api,exercise_diet_api,exercise_diet_adminSerializers
from food.views import foodAPI ,food_diet_userApi,food_diet_adminApi
from customer.views import customerAPI
from Diet.views import DietApi,Diet_adminApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercise_api/',exercise_api,name= 'exercise_api'),
    path('food_api/',foodAPI.as_view(),name= 'food_api'),
    path('customer_api/',customerAPI.as_view(),name= 'customer_api'),
    path('diet_api',DietApi.as_view(),name = 'diet_api'),
    path('exercise_diet_user',exercise_diet_api.as_view(),name = 'exercise_diet_user'),
    path('food_diet_user',food_diet_userApi.as_view(),name = 'food_diet_user'),
    path('food_diet_admin',food_diet_adminApi.as_view(),name ='food_diet_admin'),
    path('exercise_diet_admin',exercise_diet_admin_api.as_view(),name = 'exerciser_diet_admin'),
    path('Diet_adminApi',Diet_adminApi.as_view(),name='Diet_adminApi')
]
