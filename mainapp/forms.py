from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "progress_choice", "date"]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания'
            }),
            'progress_choice': Select()

        }
