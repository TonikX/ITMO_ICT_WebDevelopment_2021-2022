from django.urls import path, include

from board.views import *

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('discipline/list/', DisciplineListView.as_view(), name='discipline_list'),
    path('discipline/<int:pk>/<int:class>/', DisciplineDetailView.as_view(), name='discipline'),
    path('assignment/create/', AssignmentCreateView.as_view(), name='assignment_create'),
    path('assignment/<int:pk>/', AssignmentStudentUpdateView.as_view(), name='assignment_student_update'),
    path('assignment/grade/<int:pk>/', AssignmentGradeView.as_view(), name='assignment_grade'),
    path('assignment/delete/<int:pk>/', AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('task/list/', TaskListView.as_view(), name='task_list'),
    path('task/available/list/', TaskAvailableListView.as_view(), name='task_available_list'),
    path('task/available/list/<str:filter>/', TaskAvailableListView.as_view(), name='task_available_list_filter'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/<int:class>/', TaskDetailView.as_view(), name='task'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('class/<int:pk>/<int:discipline>/', ClassDetailView.as_view(), name='class_students'),
    path('', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
]