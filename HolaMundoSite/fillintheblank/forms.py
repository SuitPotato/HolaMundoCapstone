from django import forms

# class Create_FillInTheBlank_quiz(forms.Form):

class FillInTheBlank(forms.ModelForm):
    template_name = '/fillintheblank/fb_quiz'
    class Meta:
        model = FillInTheBlank
        fields = ('question')