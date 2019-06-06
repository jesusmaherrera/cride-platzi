"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from cride.users.serializers import (
	AcountVerificationSerializer,
	UserLoginSerializer,
	UserModelSerializer,
	UserSignUpSerializer
)

class UserLoginAPIView(APIView):
	"""User Login API view."""

	def post(self, request, *args, **kwargs):
		"""Handle HTTP POST request."""
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = {
			'user': UserModelSerializer(user).data,
			'access_token': token,
		}
		return Response(data, status=status.HTTP_201_CREATED)


class SignUpAPIView(APIView):
	"""User sign up API view."""

	def post(self, request, *args, **kwargs):
		"""Handle HTTP POST request."""
		serializer = UserSignUpSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, profile = serializer.save()
		data = UserModelSerializer(user).data
		return Response(data, status=status.HTTP_201_CREATED)


class AcountVerificationAPIView(APIView):
	"""Acount verification API view."""

	def post(self, request, *args, **kwargs):
		"""Handle HTTP POST request."""
		serializer = AcountVerificationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		data = {'message': 'Congratulation, now go share same ride!'}
		return Response(data, status=status.HTTP_200_OK)
