from django.urls import path, include

from board.views import HomeView, ProfileDetailView, DisciplineListView, DisciplineDetailView, SubmissionUpdateView

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('discipline/list', DisciplineListView.as_view(), name='discipline_list'),
    path('discipline/<int:pk>/', DisciplineDetailView.as_view(), name='discipline'),
    path('submission/<int:pk>/', SubmissionUpdateView.as_view(), name='submission'),
    path('', include('allauth.urls')),
    path('', HomeView.as_view(), name='home'),
]