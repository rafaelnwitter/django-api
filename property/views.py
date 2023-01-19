import io
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_queryset(self):
        room_id = self.kwargs.get("pk")
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

    @csrf_exempt
    def properties_list(self, request):
        if request.method == "GET":
            rooms = Rooms.objects.all()
            return rooms

    @csrf_exempt
    def room_detail(self, request, **kwargs):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            room = Rooms.objects.get(pk=pk)
        except Rooms.DoesNotExist:
            raise Http404

        if request.method == "GET":
            serializer = RoomSerializer(room)
            return JsonResponse(serializer.data)

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            serializer = RoomSerializer(room, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == "DELETE":
            room.delete()
            return HttpResponse(status=204)


@api_view(["GET", "PUT", "DELETE"])
def rooms_detail(request, pk):
    try:
        room = Rooms.objects.get(pk=pk)
    except Rooms.DoesNotExist:
        return JsonResponse(
            {"message": "The room does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        room_serializer = RoomSerializer(room)
        return JsonResponse(room_serializer.data)

    elif request.method == "PUT":
        room_data = JSONParser().parse(request)
        room_serializer = RoomSerializer(room, data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse(room_serializer.data)
        return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        room.delete()
        return JsonResponse(
            {"message": "Room was deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


class RoomDetailViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    ordering_fields = (
        "created_date",
        "price",
    )

    def room_detail(self, request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            room = Rooms.objects.get(pk=pk)
        except Rooms.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == "GET":
            serializer = RoomSerializer(room)
            return JsonResponse(serializer.data)

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            serializer = RoomSerializer(room, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == "DELETE":
            room.delete()
            return HttpResponse(status=204)
