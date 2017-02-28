from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import ModelForm
from django.db import models
# from .models import FillInTheBlank
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

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

    