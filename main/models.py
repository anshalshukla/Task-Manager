from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    assigned_to = models.ForeignKey(User, related_name="task", on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title