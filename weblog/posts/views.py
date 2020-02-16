from django.shortcuts import render

from posts.models import Post
from django.views.generic.list import ListView

"""
This is the view to display the posts in a list
"""
class PostListView(ListView):
    model = Post
    paginate_by = 5
