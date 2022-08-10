import imp
from rest_framework import serializers
from food.serializers import food_diet_user_Serializers
from exercise.serializers import exercise_dietSerializers
from Diet.models import Diet
from food.models import food
class DietSerializers(serializers.ModelSerializer):
    food_Diet = food_diet_user_Serializers(many=True)
    exercise_Diet=exercise_dietSerializers(many =True)
    class Meta:
        model= Diet
        fields = ['user','food_Diet','exercise_Diet']
        
    # def get_accounts_items(self, obj):
    #     customer_account_query = food.objects.filter(obj.id)
    #     serializer = food_diet_user_Serializers(customer_account_query, many=True)
    #     return serializer.data


