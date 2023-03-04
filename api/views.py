import math

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Trip, SustainabilityScore
from .serializers import TripSerializer, SustainabilityScoreSerializer


@api_view(["GET", "POST"])
def trips_base(request):
    if request.method == "GET":
        trips = Trip.objects.all().order_by("-created_at")
        serializer = TripSerializer(trips, many=True)

        payload = {
            "trips": serializer.data
        }

        return JsonResponse(payload)
    elif request.method == "POST":
        request_data = request.data

        if "trips" not in request_data:
            return Response("Missing trips attribute", status=status.HTTP_400_BAD_REQUEST)

        payload = []
        for trip in request_data["trips"]:
            serializer = TripSerializer(data=trip)
            if serializer.is_valid():
                destination = trip["destination"]
                try:
                    score = SustainabilityScore.objects.get(
                        destination=destination.upper()
                    )
                    if score is not None:
                        serializer.save()
                        obj = serializer.data
                        obj["sustainability_score"] = score.score
                        payload.append(obj)
                except SustainabilityScore.DoesNotExist:
                    pass

        return Response(payload, status=status.HTTP_201_CREATED)


@api_view(["GET", "POST"])
def scores_base(request):
    if request.method == "GET":

        if request.GET.get("page") is not None:
            page = int(request.GET.get("page"))
        else:
            page = 1

        if request.GET.get("per_page") is not None:
            per_page = int(request.GET.get("per_page"))
        else:
            per_page = 10

        scores = SustainabilityScore.objects.all().order_by("-created_at")

        start = (page - 1) * per_page
        end = page * per_page
        total = scores.count()
        serializer = SustainabilityScoreSerializer(scores[start:end], many=True)

        payload = {
            "scores": {
                "list": serializer.data,
                "_meta": {
                    "total": total,
                    "page": page,
                    "per_page": per_page,
                    "last_page": math.ceil(total / per_page)
                }
            },
        }

        return JsonResponse(payload)
    elif request.method == "POST":
        request_data = request.data

        if "scores" not in request_data:
            return Response("Missing scores attribute", status=status.HTTP_400_BAD_REQUEST)

        payload = []
        for score in request_data["scores"]:
            serializer = SustainabilityScoreSerializer(data=score)
            if serializer.is_valid():
                serializer.save()

                payload.append(serializer.data)

        return Response(payload, status=status.HTTP_201_CREATED)
