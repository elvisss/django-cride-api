"""Circles views"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """List circles"""
    circles = Circle.objects.filter(is_public=True)
    data = []
    for circle in circles:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'is_public': circle.is_public,
            'verified': circle.verified,
            'is_limited': circle.is_limited,
            'members_limit': circle.members_limit
        })
    return Response(data)

@api_view(['POST'])
def create_circle(request):
    """Create circle"""
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data = {
        'name': circle.name,
        'slug_name': circle.slug_name,
        'is_public': circle.is_public,
        'verified': circle.verified,
        'is_limited': circle.is_limited,
        'members_limit': circle.members_limit
    }

    return Response(data)
