from django.urls import include, path

from rest_framework import routers

from .views import PropertiesViewSet

router = routers.DefaultRouter()
router.register(r'', PropertiesViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
