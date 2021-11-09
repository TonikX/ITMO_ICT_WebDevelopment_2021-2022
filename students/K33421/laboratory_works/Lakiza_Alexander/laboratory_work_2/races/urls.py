from django.urls import path
from .views import register, index, racer, profile, race_register_add, race_register_edit, race_leave, add_commet, \
    RaceListView, RaceDetailView

urlpatterns = [
    path('', index),
    path('accounts/registration', register),
    path('race_list/', RaceListView.as_view()),
    path('race/<int:pk>/', RaceDetailView.as_view()),
    path('accounts/racer', racer, name='racer_reg'),
    path('accounts/profile', profile),
    path('race/<int:race_id>/registration', race_register_add),
    path('race/<int:race_id>/leave', race_leave),
    path('race/<int:race_id>/edit', race_register_edit),
    path('race/<int:race_id>/add_comment', add_commet)
]
