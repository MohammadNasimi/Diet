from django.shortcuts import render
from rest_framework import generics,response
from Diet.models import Diet,Diet_admin
from Diet.calculate_diet import calculate
from Diet.models import Diet,Diet_admin
# Create your views here.
from Diet.serializers import DietSerializers,Diet_adminSerializers
class DietApi(generics.ListCreateAPIView):  

    serializer_class = DietSerializers
    queryset = Diet.objects.all()

    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        Diet_data = request.data
        cal = calculate(Diet_data)
        
        print(cal[5])
        print(type(cal[5]))
        obj_diet = Diet.objects.create(user=cal[0])
        obj_diet.food_Diet.set(cal[3])
        obj_diet.exercise_Diet.set(cal[4])
        obj_diet.kind_diet = cal[5]
        obj_diet.save()
        obj_diet_admin = Diet_admin.objects.create(user_admin=cal[0])
        obj_diet_admin.food_Diet_admin.set(cal[1])
        obj_diet_admin.exercise_Diet_admin.set(cal[2])

        # food_Diet = []
        # food_diet_users = request.data.pop('food_Diet')

        # # food_diet_users = request.data.pop()
        # request.data.update({'food_Diet':food_Diet})
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data,status = 200)


class Diet_adminApi(generics.ListCreateAPIView):  

    serializer_class = Diet_adminSerializers
    # queryset = Diet_admin.objects.all()
    def get_queryset(self):
        return Diet_admin.objects.filter(user_admin=self.kwargs['customer_id'])