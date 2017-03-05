from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Preference(models.Model):

    # Autoincrement ID and user
    prefID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, blank=False)

    # Listed choices for preferences
    LANGUAGES = (
        ('English', '1'),
        ('Spanish', '2'),
    )

    DIFFICULTIES = (
        ('Beginner', '1'),
        ('Intermediate', '2'),
        ('Advanced', '3'),
    )

    # Setting preferences
    defaultLanguage = models.CharField(max_length=10, choices=LANGUAGES, default="1")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTIES, default="1")

    def __str__(self):
        return self.user.username
