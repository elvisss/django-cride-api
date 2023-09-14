"""Circles views"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle
from cride.circles.serializers import CircleModelSerializer, CreateCircleSerializer

@api_view(['GET'])
def list_circles(request):
    """List circles"""
    circles = Circle.objects.filter(is_public=True)
    serializer = CircleModelSerializer(circles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_circle(request):
    """Create circle"""
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Create circle
    circle = serializer.save()

    # Return response
    return Response(CircleModelSerializer(circle).data)
