from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.dateformat import DateFormat
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Rating


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            # Update user's email in the User model
            request.user.email = profile_form.cleaned_data['default_email']
            request.user.save()
            return redirect('profile')
    else:
        #profile_form = UserProfileForm(instance=profile)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    # Get orders related to the user profile
    orders = Order.objects.filter(user=request.user)
    # Get ratings related to the user profile
    user_ratings = Rating.objects.filter(user=request.user)

    context = {
        'profile_form': profile_form,
        'orders': orders,
        'user_ratings': user_ratings,
        'user': request.user,
    }
    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    formatted_date = DateFormat(order.date).format('j M, Y (P)')

    messages.info(request, (
        f'This is from a previous order, with order number: {order_number}. '
        f'A confirmation was sent to your email address on { formatted_date }.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
