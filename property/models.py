from django.db import models

from users.models import MyUser


class Rooms(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    guest_limity = models.PositiveIntegerField(null=False, blank=False)
    bedrooms = models.PositiveIntegerField(verbose_name="Bedrooms Avaliable", default=1)
    beds = models.PositiveIntegerField(verbose_name="Beds Avaliable", default=1)
    bathrooms = models.PositiveIntegerField(
        verbose_name="Bathrooms Avaliable", default=1, null=False, blank=False
    )
    pet_friendly = models.BooleanField(verbose_name="Are pets allowed?", null=False, blank=False, default=True)
    price = models.PositiveIntegerField(verbose_name="Price per night", null=False, blank=False, default=100)
    cleaning_fee = models.FloatField(verbose_name="Cleaning service fee", null=False, blank=False)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        verbose_name="Created Date", auto_now_add=True, editable=False
    )
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self):
        return str(self.pk)
