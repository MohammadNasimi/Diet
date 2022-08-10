from customer.serializers import customerSerializers
from customer .models import customer
from core.models import User
# Create your views here.
from rest_framework import generics , response
from django.contrib.auth import get_user_model
class customerAPI(generics.ListCreateAPIView):
    serializer_class = customerSerializers
    queryset = customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # headers = self.get_success_headers(serializer.data)
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        customer_data = request.data
        user = User.objects.create_user(username=customer_data['user']['username'],
         password=customer_data['user']['password'],kind_user =customer_data['user']['kind_user'])
        user.save()
        bmi =round(customer_data['height']/customer_data['weight'],2)
        customer_create  = customer.objects.create(user = user,age = customer_data['age']
        ,weight=customer_data['weight'],height=customer_data['height'],
        BMI=bmi)
        print(bmi)
        customer_create.save()
        # print(customer_data['user']['username'])
        # print(customer_data['age'])
        # print(customer_data['weight'])
        # print(customer_data['height'])


        return response.Response(serializer.data,status = 200)
