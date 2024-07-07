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
            email = subscribe_form.cleaned_data['email'].strip().lower()
            user = request.user if request.user.is_authenticated else None
            existing_subscription = NewsletterSubscriber.objects.filter(email=email).first()

            if existing_subscription:
                if user:
                    # Registered user with an existing subscription
                    messages.info(request, 'You are already a subscriber!')
                else:
                    # Unregistered user with an existing subscription
                    messages.error(request, 'This email is already subscribed. Please register for an account to manage your subscription.')
            else:
                # No existing subscription found, create a new one
                new_subscription = NewsletterSubscriber.objects.create(email=email, user=user)

                if user:
                    # Registered user without a subscription
                    messages.success(request, 'Excellent, you will soon get our newsletter with more inspiration!')
                else:
                    # Unregistered user without a subscription
                    messages.success(request, 'Thank you. You have successfully subscribed to the Knit&Co newsletter!')
                    return render(request, 'home/thank_you.html')  # Show thank you page for unregistered users

            return redirect(request.META.get('HTTP_REFERER', 'current_page'))  # Redirect to the referring page or current page

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

    return render(request, 'home/subscribe.html', context)


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