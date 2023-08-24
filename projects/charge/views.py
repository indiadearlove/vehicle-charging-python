from django.utils import timezone
from datetime import timedelta

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import *
@api_view(['GET', 'POST'])
def vehicle_list(request):
    if request.method == 'GET':
        data = Vehicle.objects.all()

        serializer = VehicleSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vehicle_detail(request, pk):
    if request.method == 'GET':
        data = Vehicle.objects.get(pk=pk)

        serializer = VehicleSerializer(data, context={'request': request})

        return Response(serializer.data)

@api_view(['GET'])
def stop_charge(request, pk):

    if request.method == 'GET':
        vehicle = Vehicle.objects.get(pk=pk)
        charge = vehicle.charge
        charge.end_time = timezone.now()
        charge.status = "cancelled"
        charge.save()

        Charge.objects.create(
            status="created",
            # In reality the start time would be worked out some
            # other way from the data we have about peak charging hours
            start_time=timezone.now() + timedelta(hours=1),
            expected_end_time=timezone.now() + timedelta(hours=3),
            estimated_battery_increase_percentage=20,
            vehicle=vehicle,
        )

        serializer = VehicleSerializer(vehicle, context={'request': request})

        return Response(serializer.data)

@api_view(['GET'])
def start_charge(request, pk):
    if request.method == 'GET':
        vehicle = Vehicle.objects.get(pk=pk)
        charge = vehicle.charge
        charge.delete()

        Charge.objects.create(
            status="charging",
            start_time=timezone.now(),
            estimated_battery_increase_percentage=20,
            expected_end_time=timezone.now() + timedelta(hours=1),
            vehicle=vehicle,
        )

        serializer = VehicleSerializer(vehicle, context={'request': request})

        return Response(serializer.data)