from django.contrib import admin

from ShortAnswer.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)