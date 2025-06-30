from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post, Category, Tags
from rest_framework import routers, serializers, viewsets

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

def blog(request):
    post = Post.objects.all()
    categories =  Category.objects.all()
    tags = Tags.objects.all()
    paginator = Paginator(post, 10)

    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'paginator': paginator,
        'title': 'Блог'
    }
    return render(request, 'service/blog.html', context=context)

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