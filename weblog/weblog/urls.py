"""
Definition of urls for weblog.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers

from app import forms, views
from posts import views as post_views
from comments import views as comment_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', post_views.PostViewSet)
router.register(r'comments', comment_views.CommentViewSet)

urlpatterns = [
    # Post Views
    path(
            '', 
            post_views.PostListView.as_view
            (
                extra_context = {'title': 'Posts'}
             ), 
            name='Posts'
        ),

    # Comment Views
    path(
            'comments/add/<int:post_id>/', 
            comment_views.CommentView.as_view
            (
                extra_context = {'title': 'Add Comments'}
             ), 
            name='Comments'
        ),   
    path('comments/approve/<int:post_id>/', comment_views.approve_comment , name='Approve Comments'),

    # User Views
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    # Admin Views
    path('admin/', admin.site.urls),

    # Rest Framework
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
