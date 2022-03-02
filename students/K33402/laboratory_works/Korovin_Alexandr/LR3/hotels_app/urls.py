from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view()),
    path('hotels/', HotelListView.as_view()),
    path('hotels/<int:pk>', DetailHotelView.as_view()),
    path('hotels/create', CreateHotel.as_view()),
    path('reserves/', ReserveHotelListView.as_view()),
    path('reserves/<int:pk>', DetailReserveView.as_view()),
    path('reserves/create', CreateReserveHotelView.as_view()),
    path('reviews/', ReviewHotelListView.as_view()),
    path('reviews/<int:pk>', DetailReviewView.as_view()),
    path('reviews/create', CreateReviewHotelView.as_view()),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]
