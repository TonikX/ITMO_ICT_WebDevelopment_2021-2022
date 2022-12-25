from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Car
  
class CarList(ListView):
  
    model = Car
    template_name = 'list_views_class.html'

class CarRetrieveView(DetailView):

    model = Car
    template_name = 'car_detail.html'

# class CarListView(ListView):
#     model = Car
#     template_name = 'list_views_class.html'
#     queryset = model.objects.all()

#     def get_queryset(self):
#         owner = self.request.GET.get('owner')
        
#         if owner:

#             try:
#                 owner = int(owner)
#                 queryset = self.queryset.filter(owners=owner)
                

#             except ValueError:
#                 queryset = self.model.objects.none()

#             return queryset

#         return self.queryset