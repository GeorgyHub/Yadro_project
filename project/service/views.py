from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .models import Post, Category, Tags, Comment
from rest_framework import routers, serializers, viewsets
from .forms import CommentForm, PostForm

# Create your views here.
def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'service/index.html', context=context)

def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'service/about.html', context=context)

def blog_list(request):

    post = Post.objects.all()
    categories =  Category.objects.all()
    tags = Tags.objects.all()
    paginator = Paginator(post, 10)
    form = PostForm()

    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'paginator': paginator,
        'form': form,
        'title': 'Блог'
    }
    return render(request, 'service/blog.html', context=context)

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    comment = Comment.objects.all()
    #form = CommentForm()

    context = {
        'comment': comment,
        'post': post,
        #'form': form
    }

    return render(request, 'service/post.html', context=context)

def performer(request):
    context = {
        'title': 'Исполнитель'
    }
    return render(request, 'service/performer.html', context=context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'service/contact.html', context=context)