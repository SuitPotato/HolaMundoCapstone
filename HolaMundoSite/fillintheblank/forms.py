from django import forms

# class Create_FillInTheBlank_quiz(forms.Form):

class FillInTheBlank(forms.ModelForm):
	question = forms.CharField(label='Question:')
	answer = forms.CharField(label='Answer:')

    #template_name = '/fillintheblank/fb_quiz'
    #class Meta:
    #    model = FillInTheBlank
    #    fields = ('question')