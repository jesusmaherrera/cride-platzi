"""Rides views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permisions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.memberships import IsActiveCircleMember

# Serializers
from cride.rides.serializers import CreateRideSerializer

# Models
from cride.circles.models import Circle


class RideViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Ride view set."""

    serializer_class = CreateRideSerializer
    permissions = [IsAuthenticated, IsActiveCircleMember, ]

    def dispatch(self, request, *args, **kwargs):
        """Verify that the cirle exists."""
        slug_name = kwargs['slug_name']
        self.circle = get_object_or_404(Circle, slug_name=slug_name)
        return super().dispatch(request, *args, **kwargs)

    def get_serializer_context(self):
        """Add cricle to serializer context.
        """
        context = super().get_serializer_context()
        context['circle'] = self.circle
        return context
