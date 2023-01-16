from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .serializers import PropertySerializer
from .models import Properties


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pet_friendly', 'beds', 'bedrooms', 'bathrooms']
