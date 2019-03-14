"""Django models utilities."""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    CRideModel acts as an abstract base class from wich every
    other model in the project will inherit. this class provides
    eversy table with the following attributes:
        + created (DateTime): Store the datatime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text='Date time on which the object was modified.'
    )

    class Meta:
        "Meta option."

        abstract = True
        # get_lates_by = 'created'
        ordering = ['-created', '-modified']

