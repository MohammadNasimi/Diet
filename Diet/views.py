from django.shortcuts import render
from rest_framework import generics
from Diet.models import Diet
# Create your views here.
from Diet.serializers import DietSerializers
class DietApi(generics.CreateAPIView):  

    serializer_class = DietSerializers
    queryset = Diet.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        
        Diet_data = request.data
        print(Diet_data)
        return self.create(request, *args, **kwargs)