from django.db import models

# Create your models here.
class Vocab(models.Model):
    word=models.TextField()
    meaning=models.TextField()