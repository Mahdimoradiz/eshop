from django.db import models

# Create your models here.


class Person(models.Model):
    title = models.CharField(max_length=20)