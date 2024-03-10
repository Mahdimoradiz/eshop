from django.db import models
from account.models import User



class Order(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=300)
    email = models.EmailField(blank=True, null=True)