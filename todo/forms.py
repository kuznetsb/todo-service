from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "select a date",
                "type": "datetime"
            }
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
