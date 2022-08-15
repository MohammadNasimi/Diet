import imp
from rest_framework import serializers
from food.serializers import food_diet_user_Serializers,food_diet_admin_Serializers
from exercise.serializers import exercise_dietSerializers,exercise_diet_adminSerializers
from Diet.models import Diet_admin,Diet
from food.models import food
class DietSerializers(serializers.ModelSerializer):
    food_Diet = food_diet_user_Serializers(many=True)
    exercise_Diet=exercise_dietSerializers(many =True)
    class Meta:
        model= Diet
        fields = ['user','food_Diet','exercise_Diet','kind_diet']
        
    # def get_accounts_items(self, obj):
    #     customer_account_query = food.objects.filter(obj.id)
    #     serializer = food_diet_user_Serializers(customer_account_query, many=True)
    #     return serializer.data
class Diet_adminSerializers(serializers.ModelSerializer):
    food_Diet_admin = food_diet_admin_Serializers(many=True)
    exercise_Diet_admin=exercise_diet_adminSerializers(many =True)
    class Meta:
        model= Diet_admin
        fields = ['user_admin','food_Diet_admin','exercise_Diet_admin']

