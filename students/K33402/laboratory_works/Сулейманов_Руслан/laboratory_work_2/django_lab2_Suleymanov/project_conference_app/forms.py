from django.forms import ModelForm, inlineformset_factory
from .models import Comments, Performance, Conference


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text', 'rating')


class PerformanceForm(ModelForm):

    class Meta:
        model = Performance
        fields = ('name', 'topics')