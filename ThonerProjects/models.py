from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tipe = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)