from django.contrib import admin
from .models import Grievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'name', 'email', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('tracking_id', 'name', 'email')