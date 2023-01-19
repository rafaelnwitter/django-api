from unittest import mock
import pytest
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from rest_framework.test import APIClient

from property.models import Rooms


class RoomsViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.rooms = self.rooms_create()
        self.url = reverse("rooms")
        self.url_detail = "rooms/"
       # self.url2 = reverse('rooms-detail')

    def test_list_rooms(self):
        response = self.client.get(self.url).json()
        self.assertEqual(len(response), 2)

    def test_room_pets_allowed(self):
        response = self.client.get(self.url).json()
        result = response[0]
        room_1_pets = result.get("pet_friendly")
        self.assertTrue(room_1_pets)

    def test_room_pets_not_allowed(self):
        response = self.client.get(self.url).json()
        result = response[1]
        room_2_pets = result.get("pet_friendly")
        self.assertFalse(room_2_pets)

    def test_room_delete(self):
        room = Rooms.objects.get(pk=self.rooms[1].id)
        response = self.client.delete(reverse("rooms-detail", args=[room.id]))
        self.assertEqual(response.status_code, 204)

    @pytest.mark.django_db
    def test_room_price(self):
        room = Rooms.objects.get(pk=self.rooms[0].id)
        response = self.client.get(reverse("rooms-detail", args=[room.id]))
        self.assertEqual(response.data["price"], 100)

    def rooms_create(self):
        room_1 = mommy.make(Rooms, price=100)
        room_2 = mommy.make(Rooms, pet_friendly=False)

        return [room_1, room_2]
