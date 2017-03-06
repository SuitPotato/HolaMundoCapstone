from django import forms

# class Create_FillInTheBlank_quiz(forms.Form):

class FillInTheBlank(forms.ModelForm):
	question = forms.CharField(label='Question:', max_length=250)
	answer = forms.CharField(label='Answer:', max_length=500)
    #template_name = '/fillintheblank/fb_quiz'
    #class Meta:
    #    model = FillInTheBlank
    #    fields = ('question')