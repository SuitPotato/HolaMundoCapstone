from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from Video_page.models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
