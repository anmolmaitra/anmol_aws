from django.db import models
from Exercise_Category.models import Exercise_Category

# Create your models here.
class Exercise(models.Model):
    Exercise_Name = models.TextField()
    Category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)
    Weight = models.TextField()
    Reps = models.TextField()

    def __str__(self):
        return "%s" % (self.Exercise_Name)
