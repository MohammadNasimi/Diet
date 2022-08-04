from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import response

from food.serializers import foodSerializers
# Create your views here.
from food.models import food
class foodAPI(APIView):
    def get(self,request):
        food_serializer = foodSerializers(food.objects.all(),many = True)
        return response.Response(food_serializer.data,status= 200)
    def post(self,request):
        data =request.data
        # print(data)
        food_ser = foodSerializers(data = data)
        if food_ser.is_valid():
            new_food = food_ser.save()
            return response.Response({'foodSerializers': new_food.id},status = 200)
        else:
            return response.Response( {'foodSerializers': food_ser.errors},status = 400)
