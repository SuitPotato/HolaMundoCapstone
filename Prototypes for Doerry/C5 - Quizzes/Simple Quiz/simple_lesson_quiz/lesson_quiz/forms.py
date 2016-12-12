from django import forms
from django.forms.fields import ChoiceField

from .models import BOOL_CHOICES, Lesson, LessonQuestion


class LessonQuestionForm(forms.ModelForm):
    class Meta:
        model = LessonQuestion
        widgets = {
            'correct_answer': forms.RadioSelect
        }
        fields = (
            'order_in_quiz',
            'lesson',
            'question',
            'correct_answer'
        )


class QuizQuestionField(ChoiceField):
    default_error_messages = {
        'required': 'You are required to answer this question.',
    }
    widget = forms.widgets.RadioSelect


class TakeQuizForm(forms.ModelForm):
    """
    A form for receiving answers pertaining to a Lesson.
    """
    class Meta:
        model = Lesson
        exclude = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super(TakeQuizForm, self).__init__(*args, **kwargs)
        question_list = LessonQuestion.objects.filter(
            lesson=self.instance
        ).order_by('order_in_quiz')
        for i, question in enumerate(question_list, start=1):
            self.fields[
                'question__{}'.format(question.pk)
            ] = QuizQuestionField(
                label="{num}. {question}".format(
                    num=i,
                    question=question.question
                ),
                required=True,
                choices=BOOL_CHOICES
            )
