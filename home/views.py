from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm

def index(request):
    """ Return to index page """
    
    return render(request, 'home/index.html')

def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscriptionForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(request, 'You have successfully subscribed to the Knit&Co newsletter!')
            return redirect('thank_you')
    else:
        subscribe_form = SubscriptionForm()

    context = {
        'subscribe_form':subscribe_form
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