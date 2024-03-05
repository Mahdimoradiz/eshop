from django.db import models
from tinymce.models import HTMLField
from account.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=80)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.title

class Tage(models.Model):
    title = models.CharField(max_length=80)


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/image")
    title = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)
    body = HTMLField()
    tags = models.ManyToManyField(Tage, related_name="blogs")

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return f"author by --->( {self.author} ) on --->( {self.title[:12]})"


class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]
        
    def __str__(self):
        return f"author by --->( {self.author} ) on --->( {self.post})"

    def get_absolute_url(self):
        return reverse("blog-comment-detail", kwargs={"pk": self.pk})
    
    
    