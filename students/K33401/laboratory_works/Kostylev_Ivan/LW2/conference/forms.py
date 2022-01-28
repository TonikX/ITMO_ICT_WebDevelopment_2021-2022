from django import forms
from conference.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['conference', 'description', 'rating']
