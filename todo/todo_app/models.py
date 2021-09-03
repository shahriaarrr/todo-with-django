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
    done = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now())

    def edit_title(self, new_title):
        self.title = new_title
        self.save()

    def edit_Priority(self, new_Priority):
        self.Priority = new_Priority
        self.save()

    def edit_task_text(self, new_text):
        self.task_text = new_text
        self.save()

    def edit_date(self, new_date):
        self.date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
