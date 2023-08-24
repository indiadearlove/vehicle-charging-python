from rest_framework import serializers
from .models import Vehicle


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'pk',
            'start_time',
            'end_time',
            'expected_end_time',
            'status',
        )

class VehicleSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    company_brand_colour_main = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = (
            'pk',
            'company_name',
            'company_brand_colour_main',
            'vehicle_type',
            'battery_percentage',
        )

    def get_company_name(self, obj):
        if obj.company:
            return obj.company.name

    def get_company_brand_colour_main(self, obj):
        if obj.company:
            return obj.company.brand_colour_main
