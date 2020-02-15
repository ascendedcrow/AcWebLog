"""
Definition of urls for weblog.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from posts import views as post_views
from comments import views as comment_views


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
    path(
            'comments/add/<int:post_id>/', 
            comment_views.CommentView.as_view
            (
                extra_context = {'title': 'Add Comments'}
             ), 
            name='Comments'
        ),   
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
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
    path('admin/', admin.site.urls),

]
