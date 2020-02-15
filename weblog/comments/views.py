from django.shortcuts import render

from comments.models import Comment
from django.views.generic.edit import CreateView, DeleteView, UpdateView

"""
This is the view to display the form view
"""
class CommentView(CreateView):
    model = Comment
    fields = ['post', 'name', 'e_mail', 'contents']

    def get_success_url(self):
        return '/'