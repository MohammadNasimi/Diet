import imp
from operator import ge
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import is_valid_path
from exercise.serializers import exerciseSerializers
from exercise.models import exercise ,exercise_diet_user,exercise_diet_admin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import decorators , response ,generics
from exercise.serializers import exerciseSerializers,exercise_dietSerializers,exercise_diet_adminSerializers
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from exercise.permissions import exercise_api_permission
# Create your views here.
# @csrf_exempt
# @decorators.api_view(['GET','POST'])
# def exercise_api(request):
#     if request.method == "GET":
#         exercise_list =exerciseSerializers(exercise.objects.all(),many=True)
#         return response.Response(exercise_list.data,status =200)
#     elif request.method == 'POST':
#         data =request.data
#         # print(data)
#         exercise_ser = exerciseSerializers(data = data)
#         if exercise_ser.is_valid():
#             new_exercise = exercise_ser.save()
#             return response.Response({'exercise_ser': new_exercise.id},status = 200)
#         else:
#             return response.Response( {'exercise_ser': exercise_ser.errors},status = 400)

class exercise_api(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,exercise_api_permission]
    serializer_class = exerciseSerializers
    queryset = exercise.objects.all()

class exercise_diet_api(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = exercise_dietSerializers
    queryset = exercise_diet_user.objects.all()

class exercise_diet_admin_api(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = exercise_diet_adminSerializers
    queryset = exercise_diet_admin.objects.all()
