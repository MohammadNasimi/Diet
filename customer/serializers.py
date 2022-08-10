from rest_framework import serializers

from customer.models import customer
from core.serializers import UserSerializers
class customerSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model= customer
        fields = ['user','age','weight','height','BMI']
