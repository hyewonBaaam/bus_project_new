from django.db import models

# Create your models here.
class Feed(models.Model):
    name = models.TextField()
    image = models.TextField()
    location = models.TextField()
    explain = models.TextField()
    conv = models.TextField()