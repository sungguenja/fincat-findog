from django.db import models
from accounts.models import User
from articles_lost.models import City, Borough, Animal, Species
# Create your models here.

gender_choice = (('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'))
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles_find")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = models.TextField()
    gender = models.CharField(max_length=100, choices=gender_choice)
    age = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="articles_find")
    borough = models.ForeignKey(Borough, on_delete=models.CASCADE, related_name="articles_find")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="articles_find")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="articles_find")
    time = models.CharField(max_length=100)
    image_url = models.TextField()

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_find")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments_find")