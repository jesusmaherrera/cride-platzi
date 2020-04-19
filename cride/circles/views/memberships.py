"""Circle membership views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Models
from cride.circles.models import Circle, Membership

# Serializers
from cride.circles.serializers.memberships import MembershipModelSerializer


class MembershipViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Circle Membership view set."""

    serializer_class = MembershipModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """Verify that the cirle exists."""
        slug_name = kwargs['slug_name']
        self.cirle = get_object_or_404(Circle, slug_name=slug_name)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return circle members."""
        return Membership.objects.filter(
            circle=self.cirle,
            is_active=True
        )
