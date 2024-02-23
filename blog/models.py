from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Categorie(models.Model):
      title = models.CharField(max_length=80)


class Tage(models.Model):
      title = models.CharField(max_length=100)


class Blog(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      image = models.ImageField(upload_to="blog/image")
      title = models.CharField(max_length=150)
      create_at = models.DateTimeField(auto_now_add=True)
      update_at = models.TimeField(auto_now=True)
      body = HTMLField()
      tags = models.ManyToManyField(Tage, related_name="blogs")
      
      
class BlogComment(models.Model):
      author = models.ForeignKey(User, on_delete=models.CASCADE)
      post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blogcomments')
      email = models.EmailField()
      username = models.CharField(max_length=30)
      message = models.TextField()
      date = models.DateTimeField(auto_now_add=True)