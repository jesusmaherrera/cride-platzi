"""Users views."""

# Django REST Framework
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from cride.users.serializers import (
	AcountVerificationSerializer,
	UserLoginSerializer,
	UserModelSerializer,
	UserSignUpSerializer
)

class UserViewSet(viewsets.GenericViewSet):
	"""User view set.
	Handle sign up, login and account verifications
	"""
	
	@action(detail=False, methods=['post'])
	def signup(self, request):
		"""User Sign up."""
		"""Handle HTTP POST request."""
		serializer = UserSignUpSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, profile = serializer.save()
		data = UserModelSerializer(user).data
		return Response(data, status=status.HTTP_201_CREATED)


	@action(detail=False, methods=['post'])
	def login(self, request):
		"""User Sign ip."""
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user, token = serializer.save()
		data = {
			'user': UserModelSerializer(user).data,
			'access_token': token,
		}
		return Response(data, status=status.HTTP_201_CREATED)


	@action(detail=False, methods=['post'])
	def verify(self, request):
		"""User verify."""
		serializer = AcountVerificationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		data = {'message': 'Congratulation, now go share same ride!'}
		return Response(data, status=status.HTTP_200_OK)