from rest_framework import serializers
from .models import Vehicle, Charge


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'pk',
            'start_time',
            'end_time',
            'expected_end_time',
            'estimated_battery_increase_percentage',
            'status',
        )

class VehicleSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    company_brand_colour_main = serializers.SerializerMethodField()
    charge = ChargeSerializer()

    class Meta:
        model = Vehicle
        fields = (
            'pk',
            'company_name',
            'company_brand_colour_main',
            'vehicle_type',
            'battery_percentage',
            'charge'
        )

    def get_company_name(self, obj):
        if obj.company:
            return obj.company.name

    def get_company_brand_colour_main(self, obj):
        if obj.company:
            return obj.company.brand_colour_main

