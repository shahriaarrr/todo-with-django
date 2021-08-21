from django.db import models
from django.utils import timezone

from account.models import User
# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ("h", "high"),
        ("l", "low"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    Priority = models.CharField(max_length=4, choices=PRIORITY, default="l")
    task_text = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    #rename our manager
    task = models.Manager()

    def __str__(self):
        return self.title
