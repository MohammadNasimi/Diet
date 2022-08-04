from rest_framework import serializers

from food.models import food

class foodSerializers(serializers.ModelSerializer):
    class Meta:
        model= food
        fields = ['name','calories','mesure']
