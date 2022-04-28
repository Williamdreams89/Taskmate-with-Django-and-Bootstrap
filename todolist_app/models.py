from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todolist(models.Model):
    task_manager = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    task_date = models.DateField()
    task = models.CharField(max_length=100)
    starts_from = models.TimeField()
    ends_at = models.TimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    