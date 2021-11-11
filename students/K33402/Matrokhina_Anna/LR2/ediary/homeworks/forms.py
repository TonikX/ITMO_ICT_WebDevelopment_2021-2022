from django.forms import ModelForm

from homeworks.models import HomeworkWork


class HomeworkWorkForm(ModelForm):
    class Meta:
        model = HomeworkWork
        fields = ['homework', 'text']
