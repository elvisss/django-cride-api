from django.db import models
from cride.utils.models import CRideModel
from django.urls import reverse

class Profile(CRideModel):
    """Profile model.

    A profile holds a user's public data like biography, picture
    and statistics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    # Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation based on the rides taken and offered."
    )

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)

    def get_absolute_url(self):
        """Return user's url"""
        return reverse('users:detail', kwargs={'username': self.user.username})
