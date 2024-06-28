from django.contrib import admin

from .models import Post, Category, Comment


class CommentsInline(admin.TabularInline):  # or StackedInline
    model = Comment
    fields = ['author', 'email', 'body']
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'author_information', 'author_social_link', 'category', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'body']