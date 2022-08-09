from rest_framework import serializers

from Diet.models import Diet
class DietSerializers(serializers.ModelSerializer):
    class Meta:
        model= Diet
        fields = "__all__"
