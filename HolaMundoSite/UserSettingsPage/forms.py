from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# fix this line
# from UserSettingsPage.models import UserProfile

class EditProfileForm(forms.ModelForm):
    template_name='/UserSettingsPage/edit_profile'
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
