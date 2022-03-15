from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index')),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('rooms/', include('rooms.urls')),
    path('comments/', include('comments.urls')),
    path('accounts/', include('auth.urls'))
]
