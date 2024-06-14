from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "slug",
        "preview",
        "created_at",
        "sign_publication",
        "is_published",
    )
