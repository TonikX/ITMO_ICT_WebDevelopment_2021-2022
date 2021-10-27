from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from board.models import Assignment, Task, Teacher, ClassDiscipline, Class, Student


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(required='required', maxlength='30')
        self.fields['last_name'].widget.attrs.update(required='required', maxlength='30')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class AssignmentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        class_school = kwargs.pop('class')
        student = kwargs.pop('student')
        task = kwargs.pop('task')
        super().__init__(*args, **kwargs)

        self.fields["student"].queryset = Student.objects.all().order_by(
            'class_school__name', 'user__last_name', 'user__first_name')
        if student is not None:
            self.fields["student"].initial = student
        if task is not None:
            self.fields["task"].initial = task

        try:
            teacher = Teacher.objects.all().filter(user__pk=user.pk).first()
        except AttributeError:
            return

        class_disciplines = ClassDiscipline.objects.filter(teacher=teacher.pk)
        disciplines = set(map(lambda x: x.discipline.pk, class_disciplines))
        classes = set(map(lambda x: x.class_school.pk, class_disciplines))

        self.fields["task"].queryset = Task.objects.filter(discipline__pk__in=disciplines).order_by('discipline__name')

        if class_school is not None:
            class_choices = Class.objects.filter(pk__in=classes)
            choices = ((-1, '-----'), )
            for i, elem in enumerate(classes):
                choices += ((elem, class_choices[i]), )

            self.fields["class_school"] = forms.ChoiceField(choices=choices, initial=class_school)
            self.fields["student"].required = False
            self.fields["student"].widget = forms.HiddenInput()

    class Meta:
        model = Assignment
        fields = ["task", "deadline", "student"]


class AssignmentStudentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["solution"]
        widgets = {
            'solution': forms.Textarea(attrs={'maxlength': 500, 'cols': 38, 'required': 'true'}),
        }


class AssignmentGradeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].widget.attrs.update(required='required')

    class Meta:
        model = Assignment
        fields = ["grade", "grade_comment"]
        widgets = {
            'grade_comment': forms.Textarea(attrs={'maxlength': 500, 'cols': 38}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["discipline", "title", "description"]
        widgets = {
            'description': forms.Textarea(attrs={'maxlength': 500, 'required': 'true'}),
        }
