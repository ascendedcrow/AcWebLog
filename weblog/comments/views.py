from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets

from comments.models import Comment
from posts.models import Post
from comments.serializers import CommentSerializer


class CommentView(CreateView):
    """
    This is the view to display the form view
    """
    model = Comment
    fields = ['name', 'e_mail', 'contents']

    def get_success_url(self):
        return '/'

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the post instance exists
        before going any further.
        """
        self.post_item = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_item
        return super().form_valid(form)

@login_required
def approve_comment(request, *args, **kwargs):
    """
    Approve the comment 
    """
    comment = get_object_or_404(Comment, pk=kwargs.get('post_id'))
    comment.approve_comment()
    return HttpResponseRedirect(reverse('Posts'))

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer