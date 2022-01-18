from django.urls import path
from rest_framework.routers import Route

from .views import *
from rest_framework import routers

app_name = "library_app"


# class MyRouter(routers.DefaultRouter):
#     routes = [
#         Route(
#             url=r'^{prefix}{trailing_slash}$',
#             mapping={
#                 'get': 'list',
#                 'post': 'create',
#                 'delete': 'destroy_list'
#             },
#             name='{basename}-list',
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{methodname}{trailing_slash}$',
#             name='{basename}-{methodnamehyphen}',
#             initkwargs={}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}{trailing_slash}$',
#             mapping={
#                 'get': 'retrieve',
#                 'put': 'update',
#                 'patch': 'partial_update',
#                 'delete': 'destroy'
#             },
#             name='{basename}-detail',
#             initkwargs={'suffix': 'Instance'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}/{methodname}{trailing_slash}$',
#             name='{basename}-{methodnamehyphen}',
#             initkwargs={}
#         ),
#     ]


urlpatterns = [
    path('books/', BookListAPIView.as_view()),  # list of books
    path('books/create/', BookCreateAPIView.as_view()),  # create book
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),  # book info by id

    # update / delete book by id
    path('books/edit/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),

    path('readers/', ReaderListAPIView.as_view()),  # list of readers
    path('readers/create/', ReaderCreateAPIView.as_view()),  # create reader
    path('readers/<int:pk>/', ReaderRetrieveAPIView.as_view()),  # reader info by id

    # update / delete reader by id
    path('readers/edit/<int:pk>/', ReaderRetrieveUpdateDestroyAPIView.as_view()),

    # path('report/', ReportApiView.as_view()),  # report

    path('take_out/', ReaderBookCreateAPIView.as_view()),  # take out book
    path('return/<int:pk>/', ReaderBookRetrieveUpdateDestroyAPIView.as_view()),  # return book
    path('reader_books/', ReaderBookListAPIView.as_view()),  # list of reader_book's
    path('reader_books/<int:pk>/', ReaderBookRetrieveAPIView.as_view()),  # reader_book info
]
