from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import NewsletterSubscriber

def index(request):
    """ Return to index page """
    
    return render(request, 'home/index.html')

def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscriptionForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            user = request.user if request.user.is_authenticated else None

            # Check if email is already subscribed
            existing_subscription = NewsletterSubscriber.objects.filter(email=email).first()

            if existing_subscription:
                if existing_subscription.user == user:
                    messages.info(request, 'You are already a subscriber!')
                elif existing_subscription.user is None and user:
                    # Associate the subscription with the authenticated user
                    existing_subscription.user = user
                    existing_subscription.save()
                    messages.success(request, 'You have successfully subscribed to the Knit&Co newsletter!')


            else:
                # Create a new subscription
                new_subscription = NewsletterSubscriber.objects.create(email=email, user=user)
                if user:
                    messages.success(request, 'You have successfully subscribed to the Knit&Co newsletter!')
                else:
                    messages.success(request, 'You have successfully subscribed to the Knit&Co newsletter!')
                    return render(request, 'home/thank_you.html') 

            # Redirect back to the current page
            return redirect(request.META.get('HTTP_REFERER', 'thank_you'))
        else:
            # Handle form errors
            for field, errors in subscribe_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        subscribe_form = SubscriptionForm()

    context = {
        'subscribe_form': subscribe_form
    }

    return render(request, 'home/index.html', context)


def thank_you(request):
    """ Return to thank you page """
    return render(request, 'home/thank_you.html')


def our_story(request):
    """ Return to thank you page """
    return render(request, 'home/our_story.html')


def return_policy(request):
    """ Return to thank you page """
    return render(request, 'home/return_policy.html')


def sustainability(request):
    """ Return to thank you page """
    return render(request, 'home/sustainability.html')


def cookie_policy(request):
    """ Return to thank you page """
    return render(request, 'home/cookie_policy.html')