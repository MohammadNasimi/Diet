from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import response ,generics

from food.serializers import foodSerializers,food_diet_user_Serializers,food_diet_admin_Serializers
# Create your views here.
from food.models import food ,food_diet_user,food_diet_admin
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

class food_diet_userApi(generics.ListCreateAPIView):
    serializer_class = food_diet_user_Serializers
    queryset = food_diet_user.objects.all()

class food_diet_adminApi(generics.ListCreateAPIView):
    serializer_class = food_diet_admin_Serializers
    queryset = food_diet_admin.objects.all()