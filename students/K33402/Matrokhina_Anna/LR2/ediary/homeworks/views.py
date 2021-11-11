from django.views.generic import ListView, CreateView
from .models import Homeworks, Discipline
from .forms import HomeworkWorkForm


# Create your views here.
class HomeworkListView(ListView):
    model = Homeworks
    template_name = 'index.html'


class HomeworkWorkCreateView(CreateView):
    form_class = HomeworkWorkForm
    template_name = 'homeworkwork.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.student = self.request.user

        self.object = form.save()

        return super().form_valid(form)


class DiaryListView(ListView):
    model = Discipline
    template_name = 'diary.html'
