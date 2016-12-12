from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

from .views import (
    LessonDetailView,
    LessonListView,
    QuizResultsListView,
    TakeLessonQuizView
)

urlpatterns = [
    url(r'^$', login_required(LessonListView.as_view()), name='lesson-list'),
    url(
        r'^login/$',
        login,
        {
            'template_name': 'lesson_quiz/login.html',
            'extra_context': {'next': reverse_lazy('lesson-list')}
        },
        name='login'
    ),
    url(
        r'^logout/$',
        logout,
        {'next_page': reverse_lazy('login')},
        name='logout'
    ),
    url(
        r'(?P<pk>\d+)/$',
        login_required(LessonDetailView.as_view()),
        name='lesson-detail'
    ),
    url(
        r'(?P<pk>\d+)/take-quiz/$',
        login_required(TakeLessonQuizView.as_view()),
        name='lesson-take-quiz'
    ),
    url(
        r'(?P<pk>\d+)/student-results/$',
        login_required(QuizResultsListView.as_view()),
        name='lesson-student-results'
    )
]
