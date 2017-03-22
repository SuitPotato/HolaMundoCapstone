from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from fillintheblank.forms import (
    QuestionForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def quiz(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return render(request, 'fillintheblank/success.html')
    else:
        form = QuestionForm()
    return render(request, 'fillintheblank/quiz.html', {'form': form})

#@login_required()
#def take_quiz(request, key):


''''
@login_required()
def index(request):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('fillintheblank/question.html')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/fb_quiz.html', {'form': form})

@login_required()
def detail(request):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/detail.html', {'form': form})


@login_required()
def results(request, question_id):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/detail.html', {'form': form})

    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'fillintheblank/results.html', {'question': question})

    #response = "You're looking at the results of question ."
    #return HttpResponse(response question_id)




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

    