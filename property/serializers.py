from rest_framework import serializers

from property.models import Properties


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
