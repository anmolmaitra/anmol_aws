from django.db import models

# Create your models here.
class Exercise_Category(models.Model):
    Exercise_Cat = models.TextField()

    def __str__(self):
        return "%s" % (self.Exercise_Cat)
