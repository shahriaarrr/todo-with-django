from django.db import models
# Create your models here.
class Task(models.Model):
    PRIORITY = (
        ("h", "high"),
        ("l", "low"),
    )
    title = models.CharField(max_length=15)
    Priority = models.CharField(max_length=4, choices=PRIORITY)
    task_text = models.TextField()
    date = models.DateTimeField()
    #rename our manager
    task = models.Manager()

    def __str__(self):
        return self.title
