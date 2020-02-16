import django
from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post
from django.db import transaction

class PostTest(TestCase):
    """Tests for the application views."""
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(PostTest, cls).setUpClass()
            django.setup()

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    # Models Tests
    def test_posts(self):
        post = Post()
        with transaction.atomic():
            with self.assertRaises(django.db.utils.IntegrityError):
                post.save()

        User = get_user_model()
        user = User.objects.first()

        with transaction.atomic():
            with self.assertRaises(django.db.utils.IntegrityError):
                # Duplicate check
                post = Post()
                post.title="Test"
                post.user = user
           
                post.save();

                post = Post()
                post.title="Test"
                post.user = user
           
                post.save();
        