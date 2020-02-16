from django.contrib import admin
from posts.models import Post
from comments.models import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['approved', 'name', 'e_mail', 'contents']
    

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    fields = ['title', 'contents', 'published']
    inlines = [
        CommentInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class PostAdmin(admin.ModelAdmin):
    admin.site.register(Post, PostAdmin)
