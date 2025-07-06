from django.urls import path, include
from .views import index, about, blog_list, performer, contacts, post

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('blog', blog_list, name='blog_list'),
    path('performer', performer, name="performer"),
    path('contact', contacts, name="contacts"),
    path('blog/<slug:post_slug>', post, name="post"),
]