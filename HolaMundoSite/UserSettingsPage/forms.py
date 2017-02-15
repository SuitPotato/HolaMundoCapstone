from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# fix this line
# from UserSettingsPage.models import UserProfile

class EditProfileForm(UserChangeForm):
    template_name='/UserSettingsPage/emailform'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
