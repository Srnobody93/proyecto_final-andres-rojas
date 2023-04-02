from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class entry (models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    pots_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self) :
        return self.title
