from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tage)
class TageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass
