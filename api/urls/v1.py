from django.urls import path

from api import views

urlpatterns = [
    path("trips/", views.trips_base),
    path('scores/', views.scores_base)
]
