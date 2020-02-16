import django
from django.test import TestCase
from django.contrib.auth import get_user_model

from comments.models import Comment
from posts.models import Post
from django.db import transaction

class CommentTest(TestCase):
    """Tests for the application views."""
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(CommentTest, cls).setUpClass()
            django.setup()

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    # Function Tests
    def test_functions(self):
        comment = Comment()
        User = get_user_model()
        user = User.objects.first()
        with transaction.atomic():
            post = Post()
            post.title="Test"
            post.user = user
           
            post.save();
            comment.post = post
            comment.save()    

            comment.approve_comment()

        self.assertEqual(comment.approved, True)
