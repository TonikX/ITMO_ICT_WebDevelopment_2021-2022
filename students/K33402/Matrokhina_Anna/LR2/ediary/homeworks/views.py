from django.views.generic import ListView, CreateView
from .models import Homeworks


# Create your views here.
class HomeworkListView(ListView):
    model = Homeworks
    template_name = 'index.html'


class HomeworkWorkCreateView(CreateView):
    pass
