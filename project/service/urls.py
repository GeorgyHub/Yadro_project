from django.urls import path, include
from .views import index, about, blog, performer, contacts, post

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('performer', performer, name="performer"),
    path('contact', contacts, name="contacts"),
    path('blog/<slug:post_slug>', post, name="post"),
]