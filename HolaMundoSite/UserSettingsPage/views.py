from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from UserSettingsPage.models import Preference

from UserSettingsPage.forms import (
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def settings(request):
    if request.GET.get('email') == ('email'):
        return render(request, 'UserSettingsPage/profile.html')
    elif request.GET.get('password') == ('password'):
        return render(request, 'UserSettingsPage/passwordform.html', args)
    else:
        return render(request, 'UserSettingsPage/settings.html')

@login_required()
def passwordform(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('UserSettingsPage:password')
        else:
                # if form is not valid go here
                return redirect('mainpage/DragDemo')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'UserSettingsPage/passwordform.html', {'form': form})

@login_required()
def view_profile(request):
	try:
		prefs = Preference.objects.get(user=request.user)
		args = {'user': request.user, 'prefs': prefs}
		return render(request, 'UserSettingsPage/profile.html', args)
	except:
		prefs = Preference.objects.create(user=request.user)
		prefs = Preference.objects.get(user=request.user)
		args = {'user': request.user, 'prefs': prefs}
		return render(request, 'UserSettingsPage/profile.html', args)

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            args = {'form': form}
            return render(request, 'UserSettingsPage/profile.html', args )
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'UserSettingsPage/edit_profile.html', args)
