from rest_framework import serializers

from property.models import Rooms


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
