from django.contrib import admin
from .models import *


class StoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Add a Story', {
            'fields': ('title', 'url', 'moderator'),
        }),
    )

    list_display = ('title', 'domain', 'moderator')
    list_display_links = ('title',)

# Registering sites
admin.site.register(Story, StoryAdmin)