from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def update_profile(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        update_profile_form = UserProfileForm(request.POST, instance=profile)
        if update_profile_form.is_valid():
            update_profile_form.save()
            # Update user's email in the User model
            request.user.email = update_profile_form.cleaned_data['default_email']
            request.user.save()
            return redirect('profile')
    else:
        update_profile_form = UserProfileForm(instance=profile)

    context = {
        'update_profile_form': update_profile_form,
    }
    return render(request, 'profiles/profile_update.html', context)


