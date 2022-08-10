from dataclasses import field
from rest_framework import serializers

from exercise.models import exercise ,exercise_diet_user

class exerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model= exercise
        fields = ['name_exercise','calories','time']

class exercise_dietSerializers(serializers.ModelSerializer):
    class Meta:
        model = exercise_diet_user
        fields = '__all__'
