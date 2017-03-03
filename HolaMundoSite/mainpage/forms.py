from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist


# A ModelForm automatically builds your form off a model you provide. It handles the
# validations based on the fields.
# The model User, does not need to be defined in the models.py because it is built in
# to Django.

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError("Passwords don't match.")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

