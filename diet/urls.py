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
from exercise.views import exercise_api
from food.views import foodAPI
from customer.views import customerAPI
from Diet.views import DietApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercise_api/',exercise_api,name= 'exercise_api'),
    path('food_api/',foodAPI.as_view(),name= 'food_api'),
    path('customer_api/',customerAPI.as_view(),name= 'customer_api'),
    path('diet_api',DietApi.as_view(),name = 'diet_api')
]
