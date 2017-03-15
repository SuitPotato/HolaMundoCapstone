from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
from multipleChoice.forms import (
    QuestionForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def quiz(request):
    # if request.method == 'POST':
    #     form = QuestionForm(request.POST)
    #     if form.is_valid():
    #         question = form.save()
    #         return HttpResponseRedirect('https://www.djangoproject.com/')
    #     else:
    #         return HttpResponseRedirect('https://www.djangoproject.com/')
    # else:
    #     return HttpResponseRedirect('https://www.djangoproject.com/')
    #     form = QuestionForm(request.user)
    #     return render(request, 'multipleChoice/quiz.html', {'form': form})
    # return render(request, 'multipleChoice/quiz.html', {})
    form = QuestionForm()
    return render(request, 'multipleChoice/quiz.html', {'form': form})
