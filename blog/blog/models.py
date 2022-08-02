from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    
    def __str__(self):
        return self.comment
    