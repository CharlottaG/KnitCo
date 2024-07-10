from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    fields = ('user', 'default_full_name', 'default_email', 
            'default_street_address', 'default_town_or_city', 
            'default_postcode', 'default_country', 'default_phone_number')

    readonly_fields = ('user', 'default_email',)  
    
    ordering = ('-user',)


admin.site.register(UserProfile, UserProfileAdmin)
