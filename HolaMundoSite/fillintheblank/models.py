from __future__ import unicode_literals

from django.db import models

class FillInTheBlank(models.Model):
    # title -> title of video that quiz is associated with
    title = models.CharField(max_length = 100)
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)

    class Meta:
        db_table = "FillInTheBlank"