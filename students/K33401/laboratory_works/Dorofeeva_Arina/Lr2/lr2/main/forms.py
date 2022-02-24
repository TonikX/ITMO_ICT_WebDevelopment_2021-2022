from django.forms import ModelForm, Textarea, HiddenInput
from .models import Comment


class PostComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["conference", "text", "author"]

        labels = {
            "text": "write your comment here",
        }

        widgets = {
            "conference": HiddenInput(),
            "text": Textarea(attrs={"cols": 70, "rows": 10}),
            "author": HiddenInput(),
        }
