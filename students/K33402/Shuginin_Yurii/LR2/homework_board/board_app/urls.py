from django.urls import path
from . import views

urlpatterns = [
    path('accounts/created/', views.NotificationView.as_view()),
    path('accounts/<int:pk>/update/', views.StudentUpdate.as_view()),
    path('profile/all_tasks/', views.AllTasks.as_view()),
    path('', views.StartPageView.as_view()),
    path('profile/', views.ProfilePageView.as_view()),
    path('profile/all_tasks/answer', views.solution_create),

    # path('owner/<int:car_owner_id>/', views.car_owner_info),
    # path('all_owners/', views.all_owners),
    # path('owner/create/', views.car_owner_create),
    # path('all_cars/', views.AllCars.as_view()),
    # path('car/<int:pk>/', views.CarInfo.as_view()),
    # path('car/<int:pk>/update/', views.CarUpdate.as_view()),
    # path('car/create/', views.CarCreate.as_view()),
    # path('car/<int:pk>/delete/', views.CarDelete.as_view()),
]
