from django.contrib import admin
from matching.models import Number
from matching.models import Question
from matching.models import Answer

# Register your models here.
admin.site.register(Number)
admin.site.register(Question)
admin.site.register(Answer)