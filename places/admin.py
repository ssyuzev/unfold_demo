from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import MultipleChoicesDropdownFilter, FieldTextFilter

from places.models import Location, Place


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ("name", "address", )
    search_fields = ("name", "address")


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    search_fields = ("name", "location__name")
    autocomplete_fields = ("location",)
    list_display = ("name", "location", "is_active")
    list_editable = ("location", "is_active")
    list_filter_sheet = True
    list_filter_submit = True
    list_filter = (
        ("name", FieldTextFilter),
        ("location__name", MultipleChoicesDropdownFilter),
        "is_active",
    )