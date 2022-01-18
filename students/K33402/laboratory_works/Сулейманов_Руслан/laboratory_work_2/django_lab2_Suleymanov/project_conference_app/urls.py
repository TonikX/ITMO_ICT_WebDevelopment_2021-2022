from django.urls import path
from . import views
from project_conference_app.models import Conference
from django.views.generic import ListView

urlpatterns = [
    path('',
         ListView.as_view(
             template_name='conference/conference_list.html',
             queryset=Conference.objects.all().order_by(
                '-date_end'
            ),
             paginate_by=3
         ),
         name='conference_list'),
    path('conference/<int:pk>', views.conference_detail, name='conference_detail')
]
