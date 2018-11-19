from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 10)
    location = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('posts:list')
    
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name