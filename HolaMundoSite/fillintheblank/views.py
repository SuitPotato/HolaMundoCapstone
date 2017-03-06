from django.shortcuts import render, redirect, get_object_or_404
from django.forms import *
from django.db import models
from .models import Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404


# Create your views here.

@login_required()
def index(request):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('fillintheblank/question.html')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/number.html', {'form': form})

@login_required()
def detail(request):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/detail.html' {'form': form})


@login_required()
def results(request, question_id):
    if request.method == 'POST':
        form = FillInTheBlank(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = FillInTheBlank()
        return render(request, 'fillintheblank/detail.html'{'form': form})
        
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'fillintheblank/results.html', {'question': question})

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

    