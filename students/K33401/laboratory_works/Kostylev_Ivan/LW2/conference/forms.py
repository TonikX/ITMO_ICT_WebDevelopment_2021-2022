from django import forms
from conference.models import Review, Registration


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['conference', 'description', 'rating']


class RegConfForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['conference']
