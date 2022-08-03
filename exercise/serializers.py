from rest_framework import serializers

from exercise.models import exercise

class exerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model= exercise
        fields = ['name_exercise','calories','time']
