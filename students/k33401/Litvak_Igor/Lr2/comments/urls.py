from django.urls import path
from comments.views import CommentCreateView

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='comment-create')
]
