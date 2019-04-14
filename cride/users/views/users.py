"""Users views."""

# Django REST Framework

from rest_framework import status
from rest_framework.views import APIView


# Serializers
from cride.users.serializers import UserLoginSerializer

class UserLoginAPIView(APIView):
	"""User Login API view."""

	def post(self, request, *args, **kwargs):
		"""Handle HTTP POST request."""
		serializer = UserLoginSerializer(data=request.data)
		serializer.is_valid(rise_exception=True)
		token = serializer.save()
		data = {
			'status': 'ok',
			'token': token,
		}
		return Response(data, status=status.HTTP_201.CREATED)