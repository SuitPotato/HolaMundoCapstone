from django.core.urlresolvers import reverse
from django.db import models


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    
    class Meta:
        abstract = True
        ordering = ['order',]
    
    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')
    
    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
                'course_pk': self.course_id,
                'step_pk': self.id
            })


class Quiz(Step):
    total_questions = models.IntegerField(default=4)
    
    class Meta:
        verbose_name_plural = "Quizzes"

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
                'course_pk': self.course_id,
                'step_pk': self.id
            })


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()
    
    class Meta:
        ordering = ['order',]
        
    def get_absolute_url(self):
        return self.quiz.get_absolute_url()
    
    def __str__(self):
        return self.prompt


class Answer(models.Model):
    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order',]
        
    def __str__(self):
        return self.text