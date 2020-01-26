"""Circle URLs."""

# Django
from django.urls import path

# views
from cride.circles.views import list_circles, import_circles

urlpatterns = [
    path('circles/', list_circles),
    path('circles/import/', import_circles),
]
