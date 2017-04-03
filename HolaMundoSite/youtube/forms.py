# Django Imports
from django import forms


class VidUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    Tags = forms.CharField(widget=forms.Textarea, max_length=300)



