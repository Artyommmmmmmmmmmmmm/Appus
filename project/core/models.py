from django.db import models

class File(models.Model):
    text = models.CharField(max_length=100, null=True)
    file = models.FileField()
