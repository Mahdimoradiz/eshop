from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
      pass


@admin.register(models.Tage)
class TageAdmin(admin.ModelAdmin):
      pass


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
      pass