"""Rating model."""
# django
from django.db import models

# utilities
from cride.utils.models import CRideModel


class Rating(CRideModel):
    """Ride rating.

    Rates are entities theh store the rating a user
    gave to a ride, it range from 1 to 5 and it affects
    the ride offerer's overall reputation.
    """

    ride = models.ForeignKey(
        'rides.Ride',
        on_delete=models.CASCADE,
        related_name='rated_rate',
    )
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    rating_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        help_text='User that emit the rating',
        related_name='rating_user',
    )
    related_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
    )
    comments = models.TextField(blank=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        """Return rating details."""
        return self.id
