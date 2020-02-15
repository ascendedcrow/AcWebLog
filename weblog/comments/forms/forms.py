from django.forms import ModelForm
from comments.models import Comment

"""
Create the comment form for specific fields
"""
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'e_mail', 'contents']