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
            return redirect('subscribe')
    else:
        subscribe_form = SubscriptionForm()

    context = {
        'subscribe_form':subscribe_form
    }

    return render(request, 'home/subscribe.html', context)