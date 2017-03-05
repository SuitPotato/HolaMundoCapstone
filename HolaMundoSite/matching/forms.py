from django import forms

class MatchingNumber(forms.Form):
	number = forms.IntegerField(label='How many matching questions do you want?', max_length=20)

class MatchingQuestion(forms.Form):
	question = forms.CharField(label='Question:', max_length=100)
	answer = forms.CharField(label='Answer', max_length=100)