from django.contrib import admin
from .models import NewsletterSubscriber

class NewsletterSubscriberAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email',)
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email',)
    ordering = ('-name',)

admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
