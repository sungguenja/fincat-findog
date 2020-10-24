from django.db import models
from accounts.models import User
# Create your models here.

class Animal(models.Model):
    kind = models.CharField(max_length=100)

class Species(models.Model):
    species = models.CharField(max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="species")

class City(models.Model):
    city = models.CharField(max_length=100)

class Borough(models.Model):
    gu = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="borough")

gender_choice = (('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'))
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles_lost")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = models.TextField()
    gender = models.CharField(max_length=100, choices=gender_choice)
    chip = models.BooleanField()
    age = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="articles_lost")
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE, related_name="articles_lost")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="articles_lost")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="articles_lost")
    time = models.CharField(max_length=100)
    image_url = models.TextField()

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_lost")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments_lost")
