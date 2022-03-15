from django.urls import path, re_path
from lap4 import views

urlpatterns=[
    re_path(r'^bill$',views.billApi),
    re_path(r'^bill/([0-9]+)$',views.billApi),
]