"""Cicles admin."""

# Django
from django.contrib import admin
from django.http import HttpResponse

# models
from cride.circles.models import Circle
from cride.rides.models import Ride

# Utilities
from django.utils import timezone
from datetime import datetime, timedelta
import csv


@admin.register(Circle)
class CirlceAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'is_verified',
        'is_limited',
        'members_limit',
    )
    search_fields = ('slug_name', 'name')
    list_filer = (
        'is_public',
        'is_verified',
        'is_limited',
    )
    actions = ['make_verified', 'make_unverified', 'download_todays_rides']

    def make_verified(self, request, queryset):
        """make circles verified."""
        queryset.update(is_verified=True)
    make_verified.short_description = 'Make selected Circle verified'

    def make_unverified(self, request, queryset):
        """make circles unverified."""
        queryset.update(is_verified=False)
    make_unverified.short_description = 'Make selected Circle unverified'

    def download_todays_rides(self, request, queryset):
        """Return today's rides."""
        now = timezone.now()
        start = datetime(now.year, now.month, now.day, 0, 0, 0)
        end = start + timedelta(days=1)
        rides = Ride.objects.filter(
            offered_in__in=queryset.values_list('id'),
            departure_date__gte=start,
            departure_date__lte=end,
        ).order_by('departure_date')
        response = HttpResponse(content_type='text/csv')
        response[
            'Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow([
            'id',
            'passengers',
            'departure_location',
        ])
        for ride in rides:
            writer.writerow([
                ride.pk,
                ride.passengers.count(),
                ride.departure_location
            ])
        return response
    download_todays_rides.short_description = "Download today's rides"
