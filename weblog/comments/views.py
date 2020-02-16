from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from comments.models import Comment
from posts.models import Post

"""
This is the view to display the form view
"""
class CommentView(CreateView):
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
    comment = get_object_or_404(Comment, pk=kwargs.get('post_id'))
    comment.approve_comment()
    return HttpResponseRedirect(reverse('Posts'))