from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Review(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  movie_name = models.CharField(max_length=100)
  grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)