from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tours
import datetime
  
class TourList(ListView):
  
    model = Tours
    template_name = 'list_tours.html'
    queryset = model.objects.all()
    def get_queryset(self):
        country = self.request.GET.get('country')
        
        if country:

            try:
            
                queryset = self.queryset.filter(country=country).filter(date_end__lte=datetime.date.today())
                

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset.filter(date_end__gte=datetime.date.today())

class TourRetrieveView(DetailView):

    model = Tours
    template_name = 'tour_detail.html'