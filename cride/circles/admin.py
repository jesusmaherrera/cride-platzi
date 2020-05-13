"""Cicles admin."""

# Django
from django.contrib import admin

# models
from cride.circles.models import Circle


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
    actions = ['make_verified', 'make_unverified']

    def make_verified(self, request, queryset):
        """make circles verified."""
        queryset.update(is_verified=True)
    make_verified.short_description = 'Make selected Circle verified'

    def make_unverified(self, request, queryset):
        """make circles unverified."""
        queryset.update(is_verified=False)
    make_unverified.short_description = 'Make selected Circle unverified'
