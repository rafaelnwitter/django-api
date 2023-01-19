from rest_framework import serializers

from property.models import Rooms
from users.serializers import *


class RoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer
    class Meta:
        model = Rooms
        fields = '__all__'
        depth = 2
