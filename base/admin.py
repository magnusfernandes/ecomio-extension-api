from django.contrib import admin

from .models import SustainabilityScore, Trip


# Register your models here.


@admin.register(Trip)
class LogAdmin(admin.ModelAdmin):
    readonly_fields = (
        "origin",
        "destination",
        "created_at",
    )


admin.site.register(SustainabilityScore)
