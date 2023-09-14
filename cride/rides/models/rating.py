"""Rating model."""

from django.db import models

from cride.utils.models import CRideModel

class Rating(CRideModel):
    """Rating model"""

    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE, related_name='rated_ride')
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE, related_name='rated_circle')

    rating_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, help_text="User that emits the rating", related_name='rating_user')
    rated_user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, help_text="User that receives the rating", related_name='rated_user')

    comments = models.TextField(blank=True)

    rating = models.IntegerField(default=1)

    def __str__(self):
        """Return rating and comments."""
        return f'{self.rating} {self.comments}'
