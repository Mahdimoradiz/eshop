from django.contrib import admin
from . import models


admin.site.register(models.Setting)


admin.site.site_header = "Eshop Panel"

