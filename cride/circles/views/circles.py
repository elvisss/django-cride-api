"""Circle views."""

from rest_framework import mixins, viewsets

from cride.circles.serializers import CircleSerializer

from cride.circles.models import Circle

class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
