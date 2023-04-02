from django.db import models
from django.contrib.auth.models import User



class BlogModel (models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    slug =  models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="proyecto")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
