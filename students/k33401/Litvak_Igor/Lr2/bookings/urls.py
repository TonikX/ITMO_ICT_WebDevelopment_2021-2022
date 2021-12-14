from django.urls import path
from bookings.views import BookingListView, BookingDetailView, BookingCreateView, BookingDeleteView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BookingListView.as_view(), name='booking-list'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-view'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('delete/<int:pk>', BookingDeleteView.as_view(), name='booking-delete'),
]
