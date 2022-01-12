from django.db import models
from Exercise_Category.models import Exercise_Category
from Exercise.models import Exercise


# Create your models here.
class Exercise_Day(models.Model):
    Name = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    Ex_Category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)
    Ex_Date = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.Name, self.Ex_Category)


