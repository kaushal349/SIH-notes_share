from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.TextField()
    username = models.CharField(max_length = 30)
    body = models.TextField()
    