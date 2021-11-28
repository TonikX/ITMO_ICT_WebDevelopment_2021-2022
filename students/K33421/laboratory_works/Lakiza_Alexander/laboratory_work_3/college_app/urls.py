from django.urls import path
from .views import *

app_name = "college_app"

urlpatterns = [
    path('pair/list/', PairListView.as_view()),
    path('pair/<int:pk>/', PairAllView.as_view()),
    path('pair/create/', PairCreateView.as_view()),

    path('student/list/', StudentListView.as_view()),
    path('student/<int:pk>/', StudentAllView.as_view()),
    path('student/create/', StudentCreateView.as_view()),

    path('teacher/list/', TeacherListView.as_view()),
    path('teacher/<int:pk>/', TeacherAllView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),

    path('subject/list/', SubjectListView.as_view()),
    path('subject/<int:pk>/', SubjectAllView.as_view()),
    path('subject/create/', SubjectCreateView.as_view()),

    path('subteach/list/', SubjectToTeacherListView.as_view()),
    path('subteach/<int:pk>/', SubjectToTeacherAllView.as_view()),
    path('subteach/create/', SubjectToTeacherCreateView.as_view()),

    path('mark/list/', MarkListView.as_view()),
    path('mark/<int:pk>/', MarkAllView.as_view()),
    path('mark/create/', MarkCreateView.as_view()),

]
