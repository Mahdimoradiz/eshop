from django.contrib import admin
from . import models
from django.contrib.contenttypes.admin import GenericTabularInline


class InformationAdmin(admin.StackedInline):
    model = models.Information


class ImageInline(GenericTabularInline):
    model = models.Image



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "discount", "price", "suggeste"]
    list_editable = ["discount", "price", "suggeste"]
    inlines = [
        ImageInline,
        InformationAdmin,
    ]



admin.site.register(models.Color)
admin.site.register(models.Size)

