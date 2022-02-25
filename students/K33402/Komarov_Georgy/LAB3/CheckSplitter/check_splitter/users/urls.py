from django.urls import path

from users.views import ProfileView, ProfileAvatarView

urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('profile/avatar', ProfileAvatarView.as_view()),
]
