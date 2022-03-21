from .models import Task
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ["task", "progress_choice"]

        widgets = {
            'title': TextInput(attrs={
                'class': 'task-card',
                'placeholder': 'Название задачи'
            }),
            'task': Textarea(attrs={
                'class': 'task-card',
                'placeholder': 'Описание задачи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'task-card',
                'placeholder': 'Дата создания'
            }),
            'progress_choice': Select(attrs={
                'class': 'task-card'})

        }
