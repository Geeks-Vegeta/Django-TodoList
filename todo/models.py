from django.db import models


class TaskState(models.TextChoices):
    ONGOING = 'ONGOING'
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'

# Create your models here.
class Task(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    state = models.CharField(
        max_length=20,
        choices=TaskState.choices,
        default=TaskState.PENDING,
    )

    def __str__(self):
        return self.task +" | "+ self.state



