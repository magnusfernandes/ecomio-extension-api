import uuid
from enum import Enum

from django.db import models


class VendorEnum(Enum):
    Kayak = 1
    Skyscanner = 2

    @staticmethod
    def choices():
        return [
            (1, 'Kayak'),
            (2, 'Skyscanner'),
        ]


class SustainabilityScore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination = models.CharField(max_length=10, unique=True)
    score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.destination


class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    start = models.DateField()
    end = models.DateField(null=True)

    vendor = models.IntegerField(choices=VendorEnum.choices())

    sustainability_score = models.ForeignKey(SustainabilityScore, on_delete=models.CASCADE, related_name="trips",
                                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.origin, self.destination)
