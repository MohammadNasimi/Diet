from rest_framework import serializers

from food.models import food,food_diet_user,food_diet_admin

class foodSerializers(serializers.ModelSerializer):
    class Meta:
        model= food
        fields = ['name','calories','mesure']

class food_diet_user_Serializers(serializers.ModelSerializer):
    class Meta:
        model = food_diet_user
        fields = "__all__"

class food_diet_admin_Serializers(serializers.ModelSerializer):
    class Meta:
        model = food_diet_admin
        fields = "__all__"