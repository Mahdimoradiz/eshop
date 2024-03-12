from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from tinymce.models import HTMLField

class Image(models.Model):
    image = models.ImageField(upload_to="products")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="images")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Size(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    
class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    size = models.ManyToManyField(Size, related_name="products")
    color = models.ManyToManyField(Color, related_name="products")
    image = models.ImageField(upload_to="products")
    update_at = models.DateField(auto_now=True, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    suggeste = models.BooleanField(default=False)
    more_description = HTMLField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-create_at', '-update_at']
    
    
class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="informations")
    text = models.TextField()
    
    def __str__(self):
        return self.text[:30]