from rest_framework import serializers

from base.models import Trip, SustainabilityScore


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        exclude = ["sustainability_score", "updated_at"]


class SustainabilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SustainabilityScore
        exclude = ["updated_at"]
