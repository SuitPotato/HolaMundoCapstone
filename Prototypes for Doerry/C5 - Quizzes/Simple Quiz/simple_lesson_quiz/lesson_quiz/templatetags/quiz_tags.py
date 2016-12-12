from django import template

from ..models import UserAnswer

register = template.Library()


@register.simple_tag
def has_student_completed_quiz(student, lesson):
    """
    Return a boolean signifying whether a user `student` has completed the quiz
    associated with `lesson`.
    """
    useranswer_count = UserAnswer.objects.filter(
        user_id=student.pk,
        question__in=lesson.questions.all()
    ).count()
    return bool(useranswer_count)
