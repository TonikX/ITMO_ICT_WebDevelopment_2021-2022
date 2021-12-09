from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('rooms/', include('rooms.urls')),
    path('comments/', include('comments.urls'))
]
