from django.contrib import admin
from coursemanagement.models import Lesson, Course, Quiz, CourseLessonQuiz

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(CourseLessonQuiz)
