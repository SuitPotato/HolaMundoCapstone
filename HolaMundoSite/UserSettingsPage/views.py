from django.shortcuts import render, redirect
from django.urls import reverse

from django.forms import ModelForm
from django.contrib.auth.models import User

from UserSettingsPage.forms import (
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def settings(request):
    if request.GET.get('email') == ('email'):
        return render(request, 'UserSettingsPage/emailform.html', args)
        return HttpResponseRedirect('/UserSettingsPage/emailform')
    elif request.GET.get('password') == ('password'):
        return render(request, 'UserSettingsPage/passwordform.html', args)
        return HttpResponseRedirect('/UserSettingsPage/passwordform')
    else:
        return render(request, 'UserSettingsPage/settings.html')


def passwordform(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/UserSettingsPage/settings')
        else:
            return redirect('/UserSettingsPage/passwordform')
    else:
        form = PasswordChangeForm(user = request.user)

        args = {'form':form}
        return render(request, 'UserSettingsPage/passwordform.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'UserSettingsPage/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('UserSettingsPage:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'UserSettingsPage/edit_profile.html', args)
