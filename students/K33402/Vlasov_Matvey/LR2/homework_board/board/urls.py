from django.urls import path, include

from board.views import *

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile'),

    path('discipline/list/', DisciplineListView.as_view(), name='discipline_list'),
    path('discipline/<int:pk>/<int:class>/', DisciplineDetailView.as_view(), name='discipline_student'),
    path('discipline/<int:pk>/<int:class>/<int:student>', DisciplineDetailView.as_view(), name='discipline_teacher_student'),
    path('discipline/teacher/<int:pk>/<int:class>/', DisciplineDetailView.as_view(), name='discipline_teacher'),

    path('task/available/list/', TaskAvailableListView.as_view(), name='task_available_list'),
    path('task/available/list/<str:filter>/', TaskAvailableListView.as_view(), name='task_available_list_filter'),
    path('task/<int:pk>/<int:class>/', TaskDetailView.as_view(), name='task'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),


    path('assignment/list/', AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentStudentUpdateView.as_view(), name='assignment_student_update'),
    path('assignment/create/', AssignmentCreateView.as_view(), name='assignment_create'),
    path('assignment/create/<int:student>', AssignmentCreateView.as_view(), name='assignment_student_create'),
    path('assignment/create/class/<int:class>', AssignmentCreateView.as_view(), name='assignment_class_create'),
    path('assignment/create/task/<int:task>', AssignmentCreateView.as_view(), name='assignment_task_create'),
    path('assignment/grade/<int:pk>/', AssignmentGradeView.as_view(), name='assignment_grade'),
    path('assignment/delete/<int:pk>/', AssignmentDeleteView.as_view(), name='assignment_delete'),

    path('class/<int:pk>/<int:discipline>/', ClassDetailView.as_view(), name='class_students'),
    path('', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
]