from django.shortcuts import render
from rest_framework import generics,response
from Diet.models import Diet,Diet_admin
from Diet.calculate_diet import calculate
# Create your views here.
from Diet.serializers import DietSerializers,Diet_adminSerializers
class DietApi(generics.ListCreateAPIView):  

    serializer_class = DietSerializers
    queryset = Diet.objects.all()

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        Diet_data = request.data
        print(calculate(Diet_data))
        return response.Response(serializer.data,status = 200)


class Diet_adminApi(generics.ListCreateAPIView):  

    serializer_class = Diet_adminSerializers
    queryset = Diet_admin.objects.all()