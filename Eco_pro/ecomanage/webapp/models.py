from django.db import models

# Create your models here.
class lapInfo(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    spec = models.TextField()