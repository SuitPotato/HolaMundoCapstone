from django.contrib import admin
from coursemanagement.models import Lesson, Course, Quiz, CourseLessonQuiz, MultipleChoiceQuiz, MultipleChoiceQuizResponse
from coursemanagement.models import ShortAnswerQuiz, ShortAnswerQuizResponse, MatchingQuiz

# Register your models here.
# Course Management Models
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(CourseLessonQuiz)

# Multiple Choice Models
admin.site.register(MultipleChoiceQuiz)
admin.site.register(MultipleChoiceQuizResponse)

# Short Answer Quiz models
admin.site.register(ShortAnswerQuiz)
admin.site.register(ShortAnswerQuizResponse)

# Matching Quiz Models
admin.site.register(MatchingQuiz)

