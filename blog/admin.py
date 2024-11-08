# blog/admin.py
from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published')
    list_filter = ('is_published', 'created_date')
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
