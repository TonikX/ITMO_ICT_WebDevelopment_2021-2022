from django_tables2 import tables

from hometask.models import SubmissionModel


class GradesTable(tables.Table):
    class Meta:
        model = SubmissionModel
        template_name = "django_tables2/bootstrap.html"
        fields = ("user", "hometask", "grade")