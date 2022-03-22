from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=200)
    task = models.TextField()
    progress = models.TextChoices('progress', 'Need_to_do In_progress Finish')
    progress_choice = models.CharField(blank=True, choices=progress.choices, max_length=15, default='Need_to_do')
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    # due_date = models.DateField(default=timezone.now().date())  # до какой даты нужно было сделать дело


    def __str__(self):
        return self.task
