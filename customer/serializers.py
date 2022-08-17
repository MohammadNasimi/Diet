from rest_framework import serializers

from customer.models import customer
from core.serializers import UserSerializers
from core.models import User
class customerSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model= customer
        fields = ['user','age','weight','height','BMI']

class loginserializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username','password','token']
        read_only_fields =['token']