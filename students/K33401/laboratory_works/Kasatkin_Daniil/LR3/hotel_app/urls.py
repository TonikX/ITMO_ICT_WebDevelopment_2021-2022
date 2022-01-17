from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', CreateUser.as_view()),
    path('register/host/<int:pk>', CreateHostUser.as_view()),

    path('places/', PlaceListView.as_view()),
    path('search/', PlaceListFilter.as_view(), name='place_search'),
    path('places/<int:pk>', PlaceRetrieveView.as_view()),
    path('places/create', CreatePlaceView.as_view()),

    path('reserves/', ReserveListView.as_view()),
    path('reserves/<int:pk>', ReserveRetrieveUpdateDeleteView.as_view()),
    path('reserves/create', CreateReserveView.as_view()),

    path('reviews/', ReviewListView.as_view()),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDeleteView.as_view()),
    path('reviews/create', CreateReviewView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
