from django.contrib import admin
from .models import *

# admin.site.register((Post, TopPost, MainPost))

@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov',)

@admin.register(TopPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'data', 'tanlov',)


@admin.register(MainPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'content',)



