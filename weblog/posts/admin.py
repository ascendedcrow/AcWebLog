from django.contrib import admin
from posts.models import Post
from comments.models import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['name','e_mail','contents']

class PostAdmin(admin.ModelAdmin):
    fields = ['title','contents']
    inlines = [
        CommentInline,
    ]

class PostAdmin(admin.ModelAdmin):
    admin.site.register(Post, PostAdmin)
