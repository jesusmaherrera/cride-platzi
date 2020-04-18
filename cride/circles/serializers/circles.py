"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000,
    )
    is_limited = serializers.BooleanField(default=False)

    read_only_fields = (
        'is_public',
        'verified',
        'rides_offered',
        'rides_taken',
    )

    class Meta:
        """Meta Class."""
        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'is_verified', 'is_public',
            'is_limited', 'members_limit'
        )

    def validate(self, data):
        """Ensure both members_limit and is_limited are present."""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)
        if is_limited ^ bool(members_limit):
            raise serializers.ValidationError('If cirlce is limited, a member limit must be provided.')
        return data
