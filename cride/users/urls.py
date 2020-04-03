"""Users URLs."""

# Django
from django.urls import path

# views
from cride.users.views import (
    UserLoginAPIView,
    UserSignUpAPIView,
    AcountVerificationAPIView,
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/verify/', AcountVerificationAPIView.as_view(), name='verify'),
]
