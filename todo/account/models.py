from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    GENDER_CHOICE = (
        ("w", "woman"),
        ("M", "Man"),
        ("u", "unkhow")
    )
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    age = models.PositiveIntegerField(null=True)
    description = models.TextField(max_length=1000, blank=False)