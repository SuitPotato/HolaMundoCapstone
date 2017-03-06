from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'fillintheblank/index.html', context)

    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'fillintheblank/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fillintheblank/results.html', {'question': question})

    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)



'''
def fb_quiz(request):
    # text = """<h1>welcome to my app !</h1>"""
    # return HttpResponse(text)
    if request.method == 'POST':
        form = FillInTheBlank(instance=request.POST)
        if form.is_valid():

            FillInTheBlank = form.save()
            print form.errors
            return redirect('mainpage:DragDemo')
        else:
            return redirect('mainpage:DragDemo')
    else:
        form = FillInTheBlank(instance=request.POST)
        return render(request, 'fillintheblank/fb_quiz.html', {'form':form})
'''

    