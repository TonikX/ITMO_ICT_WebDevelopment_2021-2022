from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('owner/<int:id_owner>', views.owner_id),
    path('all_owners', views.owners_all),
    path('all_cars', Cars_all.as_view()),
    path('car/<int:pk>', Car_id.as_view()),
    path('create_owner', views.owner_create),
    path('create_car', Car_create.as_view()),
    path('car/<int:pk>/update', Car_update.as_view()),
    path('car/<int:pk>/delete', Car_delete.as_view()),
]
