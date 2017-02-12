from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


# A ModelForm automatically builds your form off a model you provide. It handles the 
# validations based on the fields.
# The model User, does not need to be defined in the models.py because it is built in
# to Django.

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')