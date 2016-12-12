from distutils.util import strtobool

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Case, IntegerField, Sum, When
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views import generic

from .forms import TakeQuizForm
from .models import Lesson, UserAnswer


class RequiredGroupMixin(object):
    """
    Ensure only logged in users who belong to a particular group (or groups)
    can access this view.

    To use this Mixin, just include it as a subclass to your view and add a
    new attribute, `restrict_to_groups`, as an iterable of allowed group names.

    For example, if you want to restrict this view to only users in the group
    'Students' you'd set `restrict_to_groups` like so:

    restrict_to_groups = ('Students',)
    """
    def dispatch(self, request, *args, **kwargs):
        if hasattr(self, 'restrict_to_groups'):
            allowed_groups = request.user.groups.filter(
                name__in=self.restrict_to_groups
            )
            if not allowed_groups and request.user.is_superuser is False:
                return HttpResponseForbidden(
                    'Only users that belong to the following groups may '
                    'access this page: {}'.format(
                        ', '.join(self.restrict_to_groups)
                    ))
        return super(RequiredGroupMixin, self).dispatch(
            request, *args, **kwargs
        )


class IsStudentOrIsInstructorMixin(object):
    """
    Determines whether the logged-in user is an instructor or a student.
    """

    def dispatch(self, request, *args, **kwargs):
        is_student = False
        is_instructor = False

        if request.user.groups.filter(name__in=['Students']):
            is_student = True
        if request.user.groups.filter(
            name__in=['Instructors']
        ) or request.user.is_superuser:
            is_instructor = True

        self.is_student = is_student
        self.is_instructor = is_instructor
        return super(IsStudentOrIsInstructorMixin, self).dispatch(
            request, *args, **kwargs
        )

    def get_context_data(self, **kwargs):
        """
        Add `is_student` and `is_instructor` to the template context.
        """
        context = super(IsStudentOrIsInstructorMixin, self).get_context_data(
            **kwargs
        )

        context['is_student'] = self.is_student
        context['is_instructor'] = self.is_instructor
        return context


class LessonListView(IsStudentOrIsInstructorMixin,
                     generic.list.ListView):
    queryset = Lesson.objects.order_by('-date_created')
    template_name = 'lesson_quiz/lesson_list.html'


class LessonDetailView(IsStudentOrIsInstructorMixin,
                       generic.detail.DetailView):
    queryset = Lesson.objects.prefetch_related('questions')
    template_name = 'lesson_quiz/lesson_detail.html'


class TakeLessonQuizView(RequiredGroupMixin,
                         generic.detail.SingleObjectTemplateResponseMixin,
                         generic.edit.ModelFormMixin,
                         generic.edit.ProcessFormView):
    model = Lesson
    form_class = TakeQuizForm
    template_name = 'lesson_quiz/take_quiz.html'
    restrict_to_groups = ('Students',)

    def dispatch(self, request, *args, **kwargs):
        """
        Ensure self.object is set so TakeQuizForm instantiates correctly.
        """

        self.object = self.get_object()
        return super(TakeLessonQuizView, self).dispatch(
            request, *args, **kwargs
        )

    def convert_form_value_to_bool(self, value):
        """
        Converts a yes/no answer into a boolean
        """
        return bool(strtobool(value))

    def form_valid(self, form):
        """
        If the form is valid, record the test-taker's answers then redirect
        back to the 'Lesson List' page.
        """
        for question_key, answer in form.cleaned_data.iteritems():
            question_pk = int(question_key.split('__')[-1])
            question = self.object.questions.get(pk=question_pk)
            answer_as_bool = self.convert_form_value_to_bool(answer)
            user_answer = UserAnswer(
                user=self.request.user,
                question=question,
                answered_correctly=answer_as_bool is question.correct_answer
            )
            user_answer.save()
        return HttpResponseRedirect(reverse('lesson-list'))


class QuizResultsListView(RequiredGroupMixin,
                          generic.detail.DetailView):
    queryset = Lesson.objects.prefetch_related('questions')
    template_name = 'lesson_quiz/see_quiz_results.html'
    restrict_to_groups = ('Instructors',)

    def get_context_data(self, **kwargs):
        context = super(QuizResultsListView, self).get_context_data(**kwargs)
        context['total_questions'] = self.object.questions.count()
        context['student_list'] = User.objects.filter(
            groups__name__in=['Students'],
            quiz_answers__question__lesson_id=self.object.pk
        ).annotate(
            num_correct_answers=Sum(
                Case(
                    When(quiz_answers__answered_correctly=True, then=1),
                    default=0,
                    output_field=IntegerField()
                )
            )
        ).order_by('username').distinct()
        return context
