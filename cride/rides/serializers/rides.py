"""Rides serializer."""

from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta

from cride.rides.models import Ride
from cride.circles.models import Membership
from cride.users.serializers import UserModelSerializer


class RideModelSerializer(serializers.ModelSerializer):
    """Ride model serializer."""
    offered_by = UserModelSerializer(read_only=True)
    offered_in = serializers.StringRelatedField()

    passengers = UserModelSerializer(read_only=True, many=True)

    class Meta:
        """Meta class."""

        model = Ride
        fields = '__all__'
        read_only_fields = (
            'offered_by', 'offered_in', 'rating'
        )

    def update(self, instance, data):
        """Allow updates only before departure date."""
        now = timezone.now()
        if instance.departure_date <= now:
            raise serializers.ValidationError('Ongoing rides cannot be modified.')
        return super(RideModelSerializer, self).update(instance, data)

class CreateRideSerializer(serializers.ModelSerializer):
    """Create ride serializer."""

    offered_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    available_seats = serializers.IntegerField(min_value=1, max_value=15)

    class Meta:
        """Meta class."""

        model = Ride
        exclude = ('offered_in', 'passengers', 'rating', 'is_active')

    def validate_departure_date(self, data):
        """Verify date is not in the past."""
        min_date = timezone.now() + timedelta(minutes=10)
        if data < min_date:
            raise serializers.ValidationError('Departure date must be today or future')
        return data

    def validate(self, data):
        """Validate

        Verify that the person who offers the ride is member
        and also the same user making the request.
        """
        user = self.context['request'].user
        circle = self.context['circle']

        if data['offered_by'] != user:
            raise serializers.ValidationError('Rides offered on behalf of others are not allowed.')

        try:
            membership = Membership.objects.get(
                user=user,
                circle=circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            raise serializers.ValidationError('User is not an active member of the circle.')

        if data['arrival_date'] <= data['departure_date']:
            raise serializers.ValidationError('Departure date must happen after arrival date.')

        if data['available_seats'] < 1:
            raise serializers.ValidationError('Must be at least one seat available.')

        self.context['membership'] = membership
        return data

    def create(self, data):
        """Create ride and update stats."""
        circle = self.context['circle']
        ride = Ride.objects.create(**data, offered_in=circle)

        # Circle
        circle.rides_offered += 1
        circle.save()

        # Membership
        membership = self.context['membership']
        membership.rides_offered += 1
        membership.save()

        # Profile
        profile = self.context['request'].user.profile
        profile.rides_offered += 1
        profile.save()

        return ride
