"""Users views."""

# Django REST Framework
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

# Permissions
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated
)
from cride.users.permissions import IsAccountOwner

# Serializers
from cride.circles.serializers import CircleModelSerializer
from cride.users.serializers import (
	AcountVerificationSerializer,
	UserLoginSerializer,
	UserModelSerializer,
	UserSignUpSerializer
)

# Models
from cride.users.models import User
from cride.circles.models import Circle

membership__is_active=True

class UserViewSet(mixins.RetrieveModelMixin,
				  viewsets.GenericViewSet):
	"""User view set.
	Handle sign up, login and account verifications
	"""

	queryset = User.objects.filter(is_active=True, is_client=True)
	serializer_class = UserModelSerializer
	lookup_field = 'username' 


	def get_permissions(self):
		"""Assign permissions based on action."""
		if self.action in ['signup', 'login', 'verify']:
			permissions = [AllowAny]
		elif self.action == 'retrive':
			permissions = [IsAuthenticated, IsAccountOwner]
		else:
			permissions = [IsAuthenticated]

		return [permission() for permission in permissions]

  
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

	def retrieve(self, request, *args, **kwargs):
		"""Add extra data to the response."""
		response = super().retrieve(request, *args, **kwargs)
		circles = Circle.objects.filter(
			members=request.user,
			membership__is_active=True

		)
		data ={
			'user': response.data,
			'circles': CircleModelSerializer(circles, many=True).data
		} 
		response.data = data
		return response


	@action(detail=False, methods=['post'])
	def verify(self, request):
		"""User verify."""
		serializer = AcountVerificationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		data = {'message': 'Congratulation, now go share same ride!'}
		return Response(data, status=status.HTTP_200_OK)