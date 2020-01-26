"""Cicle model."""
# django
from django.db import models

# utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Circle model.

    A circle is a privaye group where are offered and taken
    by its members. To join a circle a user muset receive an unique
    invitation code from an existing cirlce member.
    """

    name = models.CharField('cirlce name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('cirlce description', max_length=255)
    picture = models.ImageField(
        upload_to='cirlce/pictures', blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(
        'verified cirle',
        default=False,
        help_text='Verified circle are also know as official communities.'
    )

    is_public = models.BooleanField(
        default=False,
        help_text='Public circles are listed in the main '
        'page so everyone know about their existence.'
    )
    is_limited = models.BooleanField(
        default=False,
        help_text='Limited cirlces can group to a fixed number of members.'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is Limited, this will be the limit '
        'on the number of members.'
    )

    def __str__(self):
        """Return circle name"""
        return self.name

    class Meta(CRideModel.Meta):
        """Meta class"""
        ordering = ('-rides_taken', '-rides_offered')
