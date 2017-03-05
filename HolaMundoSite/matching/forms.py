from django import forms

class MatchingNumber(forms.Form):
	number = forms.IntegerField(label='How many matching questions do you want?', max_value=26, min_value=2)

class MatchingQuestion(forms.Form):
	question = forms.CharField(label='Question:')
	answer = forms.CharField(label='Answer')
	rand_letter = forms.CharField(label='Letter')
	
class MatchingAnswer(forms.Form):
	user_answer = forms.CharField(label='Your answer:')