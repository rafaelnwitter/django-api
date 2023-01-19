from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import RoomSerializer
from .models import Rooms


class RoomsViewSet(viewsets.ModelViewSet):
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filter_fields = {
        "id": ["gte"],
        "beds": ["gt"],
        "bedsroom": ["gte"],
        "bathrooms": ["gte"],
        "price": ["gte", "lte"],
    }
    search_fields = {
        "id": ["gte"],
        "beds": ["gt"],
        "bedrooma": ["gte"],
        "bathrooms": ["gte"],
        "price": ["gte", "lte"],
    }
    ordering_fields = (
        "created_date",
        "price",
    )
    filterset_fields = ["pet_friendly", "beds", "bedrooms", "bathrooms"]
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_queryset(self):
        return Rooms.objects.all()
        
    def get_serializer_class(self):
        serializers = {
            "POST": RoomSerializer,
            "PUT": RoomSerializer,
            "PATCH": RoomSerializer,
            "GET": RoomSerializer,
        }
        return serializers.get(self.request.method)

    def destroy(self, request, *args, **kwargs):
        room_id = self.kwargs.get("pk")

        room = Rooms.objects.filter(id=room_id).first()

        if not room:
            raise Http404

        
        response = super().destroy(request, *args, **kwargs)
        
        return response

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        room_id = self.kwargs.get("pk")
        room = self.get_queryset().filter(id=room_id)

        if not room:
            raise Http404

        instance = self.get_object()

        kwargs_serializer = {"context": self.get_serializer_context()}
        serializer = RoomSerializer(instance, **kwargs_serializer)
        return Response(serializer.data)
