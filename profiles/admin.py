from django.contrib import admin
from .models import UserProfile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )
    list_filter = ('user', )

# Register models with their respective admin classes
admin.site.register(UserProfile, ProfilesAdmin)



