from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm
from .models import NewsletterSubscriber
from products.models import Product


def index(request):
    """ Return to index page """
    # Get products for display function for products with rating >=5
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)


def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscriptionForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email'].strip().lower()
            user = request.user if request.user.is_authenticated else None

            existing_subscription = NewsletterSubscriber.objects.filter(email=email).first()

            if existing_subscription:
                if user and user.email.strip().lower() == email:
                    # Logged-in user's email with an existing subscription
                    messages.info(request, 'You are already a subscriber!')
                else:
                    # Email not logged-in user, but have subscription
                    messages.info(
                        request,
                            ('This email is already subscribed. '
                            'Please provide a different email address.')
                        )
            else:
                # No existing subscription found, create a new one
                new_subscription = NewsletterSubscriber.objects.create(email=email,
                                                                        user=user if user and user.email.strip().lower() == email else None)

                if user and user.email.strip().lower() == email:
                    # Logged-in user's email without a subscription
                    messages.success(
                        request,
                            ('Excellent, you will soon get our '
                            'newsletter with more inspiration!')
                    )
                else:
                    # Different email without a subscription
                    messages.success(
                        request,
                            ('Thank you. You have successfully subscribed '
                            'to the Knit & Co newsletter!')
                    )
                    return render(request,
                                'home/thank_you.html')

        else:
            # Handle form errors
            for field, errors in subscribe_form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    return render(request, 'home/thank_you.html')


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
