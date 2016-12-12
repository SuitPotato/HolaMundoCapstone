from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

BOOL_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


@python_2_unicode_compatible
class Lesson(models.Model):
    """Represents a Lesson."""
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )
    title = models.CharField(
        _('Lesson Title'),
        max_length=140,
        help_text=_(
            'The title of this lesson.'
        )
    )
    content = models.TextField(
        _('Lesson Content'),
        help_text=_(
            'The instructional content of this lesson.'
        )
    )

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ('-date_created', '-date_modified')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class LessonQuestion(models.Model):
    """
    Represents a question pertaining to a Lesson.
    """
    lesson = models.ForeignKey(
        Lesson,
        related_name='questions'
    )
    order_in_quiz = models.PositiveIntegerField(
        _('Order in Quiz')
    )
    question = models.CharField(
        _('Question'),
        max_length=200,
        help_text=_(
            "A question that can be answered with either 'Yes' or 'No'."
        )
    )
    correct_answer = models.BooleanField(
        _('Correct Answer'),
        choices=BOOL_CHOICES,
        default=True
    )

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('order_in_quiz',)

    def __str__(self):
        return self.question


@python_2_unicode_compatible
class UserAnswer(models.Model):
    """
    Represents an answer by a user to a LessonQuestion
    """
    question = models.ForeignKey(
        LessonQuestion,
        editable=False
    )
    user = models.ForeignKey(
        'auth.User',
        editable=False,
        related_name='quiz_answers'
    )
    answered_correctly = models.BooleanField(editable=False)

    class Meta:
        verbose_name = _('User Answer')
        verbose_name_plural = _('User Answers')
        unique_together = ('question', 'user')

    def __str__(self):
        return '{} - {} - {}'.format(
            self.question_id,
            self.user_id,
            self.answered_correctly
        )
