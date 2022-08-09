from django.shortcuts import render
from rest_framework import generics,response
from Diet.models import Diet
from Diet.calculate_diet import calculate
# Create your views here.
from Diet.serializers import DietSerializers
class DietApi(generics.ListCreateAPIView):  

    serializer_class = DietSerializers
    queryset = Diet.objects.all()

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        Diet_data = request.data
        calculate(Diet_data)
        return response.Response(serializer.data,status = 200)