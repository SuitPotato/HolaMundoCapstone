# Django Imports
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# User Settings Imports
from UserSettingsPage.models import Preference
from UserSettingsPage.forms import (
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def view_my_profile(request):
    name = request.user.username
    try:
        prefs = Preference.objects.get(user=request.user)
    except:
        prefs = Preference.objects.create(user=request.user)
        prefs = Preference.objects.get(user=request.user)

    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("savebutton") == "Save User info":
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                f = form.save(commit=False)
                f.username = name
                f.save()
                context = {'type': 'success', 'notification': ', your user settings have been successfully updated.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)
            else:
                context = {'type': 'danger', 'notification': ', problem updating your user info. Try again later.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)
        elif request.POST.get("savebutton") == "Save Password":
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                context = {'type': 'success', 'notification': ', your password been successfully updated.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)
            else:
                context = {'type': 'danger',
                           'notification': ', problem updating your password. Try using a more complex password.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)
        elif request.POST.get("savebutton") == "Save User Prefs":
            try:
                prefs = Preference.objects.get(user=request.user)
                prefs.defaultLanguage = prefs.LANGUAGES[int(request.POST['user_language']) - 1][0]
                prefs.difficulty = prefs.DIFFICULTIES[int(request.POST['user_difficulty']) - 1][0]
                prefs.save()
                context = {'type': 'success', 'notification': ', your user preferences have been successfully updated.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)
            except:
                context = {'type': 'danger', 'notification': ', problem updating your preferences. Try again later.',
                           'user': request.user, 'prefs': prefs}
                return render(request, 'UserSettingsPage/myProfile.html', context)

    else:
        try:
            prefs = Preference.objects.get(user=request.user)
            args = {'user': request.user, 'prefs': prefs}
            return render(request, 'UserSettingsPage/myProfile.html', args)
        except:
            prefs = Preference.objects.create(user=request.user)
            prefs = Preference.objects.get(user=request.user)
            args = {'user': request.user, 'prefs': prefs}
            return render(request, 'UserSettingsPage/myProfile.html', args)
