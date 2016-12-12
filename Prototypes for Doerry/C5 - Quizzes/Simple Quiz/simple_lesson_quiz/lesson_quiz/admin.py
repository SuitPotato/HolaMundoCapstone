from django.contrib import admin

from .forms import LessonQuestionForm
from .models import Lesson, LessonQuestion


class LessonQuestionStackedInline(admin.StackedInline):
    form = LessonQuestionForm
    model = LessonQuestion
    ordering = ("order_in_quiz",)
    extra = 1


class LessonModelAdmin(admin.ModelAdmin):
    inlines = [LessonQuestionStackedInline]


admin.site.register(Lesson, LessonModelAdmin)
