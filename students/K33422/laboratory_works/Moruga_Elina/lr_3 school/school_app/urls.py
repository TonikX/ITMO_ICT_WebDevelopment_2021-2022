from django.urls import path
from .view_teacher import *
from .view_student import *
from .view_grades import *
from .view_timetable import *
from .view_subject import *
from .view_room import *


urlpatterns = [
    path('teachers/list/', TeacherAPIView.as_view()),
    path('teachers/create/', TeacherCreateView.as_view()),
    path('students/list/', StudentAPIView.as_view()),
    path('students/create/', StudentCreateView.as_view()),
    path('students/delete/<int:pk>/', StudentDelete.as_view()),
    path('students/update/<int:pk>/', StudentUpdate.as_view()),
    path('teachers/delete/<int:pk>/', TeacherDelete.as_view()),
    path('teachers/update/<int:pk>/', TeacherUpdate.as_view()),
    path('grades/list/', GradesAPIView.as_view()),
    path('grades/create/', GradesCreateView.as_view()),
    path('grades/update/<int:pk>/', GradesUpdate.as_view()),
    path('timetable/create/', TimetableCreateView.as_view()),
    path('timetable/', TimetableAPIView.as_view()),
    path('timetable/update/<int:pk>/', TimetableUpdate.as_view()),
    path('subjects/', SubjectAPIView.as_view()),
    path('rooms/', RoomAPIView.as_view()),
]