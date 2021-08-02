from django.db import models

# Create your models here.
class Capital(models.Model):
    name=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    pin=models.CharField(max_length=122)