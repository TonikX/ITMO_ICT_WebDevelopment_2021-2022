from django.urls import path
from .views import *

app_name = "library_app"

urlpatterns = [
    path('book/list/', BookListAPIView.as_view()),
    path('book/create/', BookCreateAPIView.as_view()),
    path('book/<int:pk>/update/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/<int:pk>', ReaderRetrieveAPIView.as_view()),
    path('readers/create/', ReaderCreateAPIView.as_view()),
    path('readers/<int:pk>/update/', ReaderRetrieveUpdateDestroyAPIView.as_view()),
    path('halls/list/', HallsListAPIView.as_view()),
    path('halls/create/', HallsCreateAPIView.as_view()),
    path('halls/<int:pk>/update/', HallsRetrieveUpdateDestroyAPIView.as_view()),
    path('book_attachment/list/', BookAttachmentListAPIView.as_view()),
    path('book_attachment/create/', BookAttachmentCreateAPIView.as_view()),
    path('book_attachment/<int:pk>/update/', BookAttachmentRetrieveUpdateDestroyAPIView.as_view()),
    path('readers/<int:pk>/books/', ReaderBookRelated.as_view()),  
    path('readers_attachment/list/', ReadersAttachmentAPIView.as_view()),
    path('readers_attachment/create/', ReadersAttachmentCreateAPIView.as_view()),
    path('readers_attachment/<int:pk>/update/', ReadersAttachmentRetrieveUpdateDestriyAPIView.as_view())
    ]