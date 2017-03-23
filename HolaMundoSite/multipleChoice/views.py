from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from multipleChoice.models import Question
from multipleChoice.forms import (
    QuestionForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quiz(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
    else:
        form = QuestionForm()
    return render(request, 'multipleChoice/quiz.html', {'form': form})

def takeQuiz(request):
    quiz = Question.objects.all()
    return render(request, 'multipleChoice/takeQuiz.html', {"quiz": quiz})
