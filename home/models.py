from django.db import models



class Setting(models.Model):
    logo = models.ImageField(upload_to="site/settings")
    phone = models.IntegerField()
    