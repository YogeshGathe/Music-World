from turtle import title
from django.db import models

# Create your models here.
class Chord(models.Model):
    title = models.CharField(max_length=200)
    singer = models.CharField(max_length=100)
    chord = models.CharField(max_length=50)

    def __str__(self):
        return self.title