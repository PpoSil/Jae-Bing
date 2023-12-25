from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    date_of_birth=models.DateField(default="1994-02-23")
    followers = models.ManyToManyField(
        'self',
        related_name='following',
        symmetrical=False
    )
    followers_count = models.PositiveIntegerField(default=0)