from django.db import models

# Create your models here.
class Animal_Picture(models.Model):
    picture = models.ImageField(upload_to='images/')