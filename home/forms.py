from django import forms
from .models import NewsletterSubscriber

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['name', 'email']