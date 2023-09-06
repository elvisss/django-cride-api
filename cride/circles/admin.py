"""Circle models admin."""

from django.contrib import admin
from cride.circles.models import Circle

@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle model admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit'
    )
    list_filter = (
        'is_public',
        'verified',
        'is_limited'
    )
    search_fields = (
        'slug_name',
        'name'
    )
