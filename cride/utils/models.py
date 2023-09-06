"""Django models utilities"""

from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    Abstract class that includes configurations common to all the models in the project.
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
