from django.db import models


# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=50)
    blog_id = models.CharField(max_length=50)
    
    def __str__(self):
        return self.comment
    