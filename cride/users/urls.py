"""Users URLs.."""
# Django
from django.urls import path

# Views
from cride.users.views import UserLoginAPIView, SignUpAPIView

urlpatterns = [
		path('users/login/', UserLoginAPIView.as_view(), name='login'),	
		path('users/signup/', SignUpAPIView.as_view(), name='signup'),	
]