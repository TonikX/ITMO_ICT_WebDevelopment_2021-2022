from django import forms
from board_app.models import TaskCompletion


class SolutionForm(forms.ModelForm):

    class Meta:
        model = TaskCompletion
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'maxlength': 500, 'cols': 38, 'required': 'true'}),
        }

    def __init__(self, task, user, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.homework = task
        self.student = user
    
    def save(self, commit=True):
        instance = super(SolutionForm, self).save(commit=False)
        if not instance.homework_id:
            instance.homework = self.homework
            instance.student = self.student
        if commit:
            instance.save()
        return instance