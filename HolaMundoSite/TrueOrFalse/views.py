from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def index(request):
	question_list = Question.objects.all()
	template = loader.get_template('TrueOrFalse/index.html')
	context = {
        'question_list': question_list,
    }
	return render(request, 'TrueOrFalse/index.html', context)
	
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'TrueOrFalse/detail.html', {'question': question})
	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'TrueOrFalse/results.html', {'question': question})
	
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'TrueOrFalse/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		if(selected_choice != answer_text):
			print("Incorrect")
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('TrueOrFalse:results', args=(question.id,)))
		