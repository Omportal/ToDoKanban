from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    task = models.TextField()
    progress = models.TextChoices('progress', 'Need_to_do In_progress Finish')
    progress_choice = models.CharField(blank=True, choices=progress.choices, max_length=15, default='Need_to_do')
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.task
