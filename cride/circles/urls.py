"""Circle URLs.."""
# Django
from django.urls import path

# Views
from cride.circles.views import list_circles, create_circlce

urlpatterns = [
		path('circles/', list_circles),
		path('circles/create/', create_circlce),
]