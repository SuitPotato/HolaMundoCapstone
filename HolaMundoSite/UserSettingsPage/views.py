from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash # keeps user logged in after password change
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.http import HttpResponse

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

def emailform(request):
    if request.method == 'POST':
        form = EditProfileForm(data = request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/UserSettingsPage/settings')
            # redirect users to profile page
            # return redirect(reverse(''))
            # args = {'form':form}
            # return render(request, 'mainpage/index.html', args)
            # return HttpResponseRedirect('/mainpage/index.html')
        else:
            form = EditProfileForm(user=request.user)
            args = {'form':form}
            return render(request, 'UserSettingsPage/emailform.html', args)
