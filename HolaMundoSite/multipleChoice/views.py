from django.shortcuts import render
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
    if request.method == 'POST':
        form = QuestionForm(request.question, request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('www.djangoproject.com')
        else:
            return redirect('mainpage/DragDemo')
    else:
        form = QuestionForm(request.question)
        return render(request, 'multipleChoice/quiz.html', {'form': form})
    return render(request, 'multipleChoice/quiz.html', {})
