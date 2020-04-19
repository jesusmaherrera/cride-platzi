"""Circle URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circle_views
from .views import memberships as membership_views

router = DefaultRouter()

router.register(r'circles', circle_views.CircleViewSet, basename='cirlces')
router.register(
    r'circles/(?P<slug_name>[a-z-A-Z-0-0_]+)/members',
    membership_views.MembershipViewSet,
    basename='mermbership'
)

urlpatterns = [
    path('', include(router.urls)),
]
