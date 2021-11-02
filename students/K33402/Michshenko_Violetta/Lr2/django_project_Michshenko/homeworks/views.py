from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Homework
from .forms import DoneForm
from django.views.generic.edit import CreateView
from django.shortcuts import render

# Create your views here.
class HomeworkListView(ListView):
    model = Homework
    template_name = 'homeworks.html'

class DoneCreateView(CreateView):
    form_class = DoneForm
    template_name = 'doneform.html'
    success_url = '/homeworks'

    def form_valid(self, form):
        form.instance.student = self.request.user

        self.object = form.save()

        return super().form_valid(form)


def marks(request):
    data = []
    homeworks = Homework.objects.all()
    
    for hw in homeworks:
        students = {}
        for hw_done in hw.done_set.all():
            if not (hw_done.student.username in students):
                students[hw_done.student.username] = []
            students[hw_done.student.username].append(hw_done.mark)

        data.append({'homework': hw, 'students': students})

    return render(request, 'marks.html', context={'data': data})
