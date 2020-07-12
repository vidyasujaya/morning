from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    COLOR_CHOICES = (
        ("Yellow", "Yellow"),
        ("Blue", "Blue"),
        ("Red", "Red"),
        ("Green", "Green"),
        ("Pink", "Pink"),
        ("Purple", "Purple"),
        ("Orange", "Orange"),
    )

    title = models.CharField(blank=False, max_length=100)
    color = models.TextField(choices=COLOR_CHOICES)

    def __str__(self):
        return self.title

class Task(models.Model):
    
    title = models.CharField(blank=False, max_length=100)
    category = models.ManyToManyField(Category)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task', blank=False)

    def __str__(self):
        return self.title
