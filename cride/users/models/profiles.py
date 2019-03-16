"""Profile model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Profile(CRideModel):
	"""Profile model.
	
	A profile holds a user's public data like biography, picture,
	and statics.
	"""

	users = models.OneToOneField('users.User', on_delete=models.CASCADE)

