from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView

from hometask.forms import SubmissionForm
from hometask.models import HometaskModel, GroupModel, SubmissionModel
from hometask.tables import GradesTable


class HometaskList(ListView):
    model = HometaskModel
    template_name = 'hometask_list_view.html'


@login_required
def submission(request):
    context = {}
    form = SubmissionForm(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.user = request.user
        try:
            data.save()
            form = SubmissionForm()  # clean the form
        except IntegrityError:
            messages.error(request, "You can't submit task again")
    context['form'] = form
    return render(request, "hometask_submission.html", context)


class GroupList(ListView):
    model = GroupModel
    template_name = 'group_list_view.html'


class GradesTableView(SingleTableView):
    model = SubmissionModel
    table_class = GradesTable
    queryset = SubmissionModel.objects.all()
    template_name = 'grades_table_view.html'

    def get_queryset(self):
        group = self.kwargs['group']
        if group:
            try:
                group = int(group)
                queryset = self.queryset.filter(user__group=group)
            except ValueError:
                queryset = self.model.objects.none()
            return queryset
        return self.queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        group = self.kwargs['group']
        context["group"] = GroupModel.objects.get(id=group)
        return context

