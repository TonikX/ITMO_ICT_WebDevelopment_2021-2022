from django.views.generic.list import ListView
from .models import Reviews, Tours

  
class ReviewList(ListView):
  
    model = Reviews
    template_name = 'list_reviews.html'
    queryset = model.objects.all()
 
    def get_queryset(self):
       tour = self.request.GET.get('tour')
 
       if tour:
           tour = Tours.objects.all().filter(id=tour)
 
           queryset = self.queryset.filter(id_tour=tour)
 
       return self.queryset