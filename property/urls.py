from django.urls import path
from .views import RoomsViewSet

_READY_ONLY = {"get": "list"}

_LIST = {"get": "list", "post": "create"}

_DETAIL = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
}

_ONLY_DELETE = {"delete": "destroy"}


urlpatterns = [
    path('', RoomsViewSet.as_view(_LIST), name="rooms"),
    path("<str:pk>", RoomsViewSet.as_view(_DETAIL), name="rooms-detail"),
]
