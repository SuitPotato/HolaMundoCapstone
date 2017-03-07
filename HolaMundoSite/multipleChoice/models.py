from __future__ import unicode_literals

from django.db import models


class Questions(models.Model):
    question = models.CharField(max_length=150)

class Answers(models.Model):
    answer_a = models.CharField(max_length=150)
    answer_b = models.CharField(max_length=150)
    answer_c = models.CharField(max_length=150)
    answer_d = models.CharField(max_length=150)
