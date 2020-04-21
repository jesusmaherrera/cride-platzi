"""Rides URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import rides as rides_views

router = DefaultRouter()

router.register(
    r'circles/(?P<slug_name>[a-z-A-Z-0-0_]+)/rides',
    rides_views.RideViewSet,
    basename='rides'
)

urlpatterns = [
    path('', include(router.urls)),
]
