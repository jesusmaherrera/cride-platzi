"""User serializers."""

# Django
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
	"""User login serializer.

	Handle the login request data.
	"""

	email = serializers.EmailField()
	password = serializers.CharField(min_length=8, max_length=64)

	def validate(self, data):
		"""Check credientials."""
		user = authenticate(username=data['email'], data['password'])
		if not user:
			raise serializers.ValidationError('Invalid credientials')
		return data
