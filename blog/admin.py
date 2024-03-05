from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "create_at"]
    list_filter = ["create_at", "update_at"]


@admin.register(models.Tage)
class TageAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]



@admin.register(models.BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ["author", "post", "date", "active"]
    list_filter = ["active"]
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)