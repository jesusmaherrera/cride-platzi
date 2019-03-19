"""Circle model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Circle(CRideModel):
	"""Circle model.

	A circle is a private group where ride are offered and taken
	by its members. To join a circle a user most recive an unique
	invitation code from an existing circle member.
	"""

	name = models.CharField('circle name', max_lenght=140)
	slug_name = models.SlugField(unique=True, max_lenght=40)

	about = models.CharField('circle description', max_lenght=255)
	picture = models.ImageField(upload_to='circles/pictures', blanck=True, null=True)

	# Stats
	rides_offered = models.PositiveIntegerField(default=0)
	rides_taken = models.PositiveIntegerField(default=0)

	verified = models.BooleanField(
		'verified circle',
		default=False,
		help_text='Verified circles are also known as official comumnities'
	)

	is_public = models.BooleanField(
		default=True,
		help_text='Public cricles are listed in the main page so everyone know about their existence.'
	)

	is_limited = models.BooleanField(
		'limited',
		default=False,
		help_text='LImited circles can grouw up to a fixed number of members.'
	)
	members_limit = models.PositiveIntegerField(
		default=0,
		help_text='If circle is limited, this will be the limit on the number of memebers.'
	)

	def __str__(self):
		"""Return cirlce name."""
		return self.name

	class Meta(CRideModel.Meta):
		"""Meta Class."""

		ordering = ['-rides_taken', '-rides_offered' ]


