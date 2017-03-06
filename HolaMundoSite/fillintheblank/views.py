from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from .models import Question
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)



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

    