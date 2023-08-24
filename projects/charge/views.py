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