from rest_framework import serializers
from .models import Grievance


class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = [
            'id',
            'tracking_id',
            'name',
            'email',
            'complaint',
            'category',
            'status',
            'priority',
            'photo',
            'latitude',
            'longitude',
            'created_at',
        ]