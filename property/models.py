import uuid
from django.db import models


class Properties(models.Model):
    guest_limity = models.IntegerField(null=False, blank=False)
    bedrooms = models.IntegerField(verbose_name="Bedrooms Avaliable", default=1)
    beds = models.IntegerField(verbose_name="Beds Avaliable", default=1)
    bathrooms = models.IntegerField(
        verbose_name="Bathrooms Avaliable", default=1, null=False, blank=False
    )
    pet_friendly = models.BooleanField(verbose_name="Are pets allowed?", null=False, blank=False, default=True)
    cleaning_fee = models.FloatField(verbose_name="Cleaning service fee", null=False, blank=False)
    created_date = models.DateTimeField(
        verbose_name="Created Date", auto_now_add=True, editable=False
    )
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)
