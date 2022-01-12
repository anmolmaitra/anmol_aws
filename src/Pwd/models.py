from django.db import models

# Create your models here.
class Pwd(models.Model):
    SName = models.TextField()
    SURL = models.TextField(blank=True, null=True)
    SUserName = models.TextField()
    SPwd = models.TextField()
    SNotes = models.TextField(blank=True, null=True)