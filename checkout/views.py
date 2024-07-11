from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json

from decimal import Decimal


def cache_checkout_data(request):
    """ Capture metadata in payment intent """
    try:
        client_secret = request.POST.get('client_secret')
        pid = client_secret.split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 
                'Sorry, your payment cannot be processed. Please try again later.')
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    intent = None
    initial_data = {}

    # Check if user is authenticated to prepopulate form
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        initial_data = {
            'full_name': profile.default_full_name,
            'email': profile.default_email,
            'phone_number': profile.default_phone_number,
            'country': profile.default_country,
            'postcode': profile.default_postcode,
            'town_or_city': profile.default_town_or_city,
            'street_address': profile.default_street_address,
        }

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # If user is logged in, update form_data with user data
        if request.user.is_authenticated:
            form_data = {
                'full_name': request.POST.get('full_name',
                            profile.default_full_name),
                'email': request.POST.get('email', profile.default_email),
                'phone_number': request.POST.get('phone_number',
                            profile.default_phone_number),
                'country': request.POST.get('country',
                            profile.default_country),
                'postcode': request.POST.get('postcode',
                            profile.default_postcode),
                'town_or_city': request.POST.get('town_or_city',
                            profile.default_town_or_city),
                'street_address': request.POST.get('street_address',
                            profile.default_street_address),
            }
        else:
            form_data = {
                'full_name': request.POST.get('full_name', ''),
                'email': request.POST.get('email', ''),
                'phone_number': request.POST.get('phone_number', ''),
                'country': request.POST.get('country', ''),
                'postcode': request.POST.get('postcode', ''),
                'town_or_city': request.POST.get('town_or_city', ''),
                'street_address': request.POST.get('street_address', ''),
            }

        # Use data=form_data to populate the form
        order_form = OrderForm(data=form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            client_secret = request.POST.get('client_secret') 
            pid = client_secret.split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)

            # Assign user if logged in
            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:

                    messages.error(request,
                            "One of the products in your bag wasn't found in our database.")
                    order.delete()

                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST

            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        else:
            messages.error(request,
                    'There was an error with your form. Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request,
                        "There's nothing in your bag at the moment.")
            return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = Decimal(current_bag['total'])
    delivery_cost = total * Decimal('0.1')
    grand_total = total + delivery_cost
    stripe_total = round((total + delivery_cost) * Decimal('100'))
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=int(stripe_total),
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request,
                    'Stripe public key is missing. Did you forget to set it in your environment?')

    context = {
        'order_form': order_form if 'order_form' in locals() else OrderForm(initial=initial_data),
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'delivery_cost': delivery_cost, 
        'grand_total': grand_total, 
        'total' : total,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Get user profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user = request.user
        order.save()

        # Save user info (email is conected to login)
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_street_address': order.street_address,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_country': order.country,
            }

            user_profile_form = UserProfileForm(profile_data,
                instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Nice stuff, we will pack it asap! \
        Your order number is {order_number}.')

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
