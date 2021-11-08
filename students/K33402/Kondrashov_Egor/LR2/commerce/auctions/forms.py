from django import forms
from .models import ListingComment


class ListingCommentForm(forms.ModelForm):
    class Meta:
        model = ListingComment
        fields = ['text']
