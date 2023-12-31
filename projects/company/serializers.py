from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'pk',
            'name',
            'brand_colour_main',
        )
