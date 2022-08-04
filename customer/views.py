from django.shortcuts import render
from customer.serializers import customerSerializers
from customer .models import customer
# Create your views here.
from rest_framework import generics , response

class customerAPI(generics.ListCreateAPIView):
    serializer_class = customerSerializers
    queryset = customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=200, headers=headers)