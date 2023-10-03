from django.contrib import admin

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
