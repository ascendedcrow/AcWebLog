from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer

class PostListView(ListView):
    """
    This is the view to display the posts in a list
    """
    model = Post
    paginate_by = 5


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer