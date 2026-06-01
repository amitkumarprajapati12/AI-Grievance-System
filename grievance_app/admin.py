from django.contrib import admin
from django.utils.html import format_html
from .models import Grievance


@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):

    list_display = (
        'tracking_id',
        'name',
        'email',
        'category',
        'status',
        'priority',
        'photo_preview',
        'location_link',
        'created_at'
    )

    list_filter = (
        'status',
        'category',
        'priority',
        'created_at'
    )

    search_fields = (
        'tracking_id',
        'name',
        'email',
        'complaint'
    )

    readonly_fields = (
        'tracking_id',
        'photo_preview',
        'location_link',
        'created_at'
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" height="60" style="border-radius:8px; object-fit:cover;" />',
                obj.photo.url
            )
        return "No Photo"

    photo_preview.short_description = "Photo"

    def location_link(self, obj):
        if obj.latitude and obj.longitude:
            return format_html(
                '<a href="https://www.google.com/maps?q={},{}" target="_blank">View Map</a>',
                obj.latitude,
                obj.longitude
            )
        return "No Location"

    location_link.short_description = "Location"