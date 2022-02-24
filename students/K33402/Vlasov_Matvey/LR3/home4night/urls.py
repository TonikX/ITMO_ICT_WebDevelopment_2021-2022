from django.urls import path

from .views import *


urlpatterns = [
   path('user/<int:pk>', UserRetrieveView.as_view()),
   path('user/list/', UserListView.as_view()),
   path('user/create/', UserCreateView.as_view()),
   path('user/update/<int:pk>', UserUpdateView.as_view()),
   path('user/delete/<int:pk>', UserDestroyView.as_view()),

   path('landlord/<int:pk>', LandlordRetrieveView.as_view()),
   path('landlord/list/', LandlordListView.as_view()),
   path('landlord/create/', LandlordCreateView.as_view()),
   path('landlord/delete/<int:pk>', LandlordDestroyView.as_view()),

   path('tenant/<int:pk>', TenantRetrieveView.as_view()),
   path('tenant/list/', TenantListView.as_view()),
   path('tenant/create/', TenantCreateView.as_view()),
   path('tenant/delete/<int:pk>', TenantDestroyView.as_view()),

   path('property/<int:pk>', PropertyRetrieveView.as_view()),
   path('property/list/', PropertyListView.as_view()),
   path('property/create/', PropertyCreateView.as_view()),
   path('property/update/<int:pk>', PropertyUpdateView.as_view()),
   path('property/delete/<int:pk>', PropertyDestroyView.as_view()),

   path('booking/<int:pk>', BookingRetrieveView.as_view()),
   path('booking/list/', BookingListView.as_view()),
   path('booking/create/', BookingCreateView.as_view()),
   path('booking/update/<int:pk>', BookingUpdateView.as_view()),
   path('booking/delete/<int:pk>', BookingDestroyView.as_view()),

   path('review/<int:pk>', ReviewRetrieveView.as_view()),
   path('review/list/', ReviewListView.as_view()),
   path('review/create/', ReviewCreateView.as_view()),
   path('review/update/<int:pk>', ReviewUpdateView.as_view()),
   path('review/delete/<int:pk>', ReviewDestroyView.as_view()),
]