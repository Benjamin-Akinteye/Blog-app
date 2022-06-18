from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    Text = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title