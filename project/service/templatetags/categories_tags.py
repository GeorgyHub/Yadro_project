from service.models import Category, Comment
from django import template
from django.db.models import Count, F

register = template.Library()

@register.simple_tag(name='getcat')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('service/blog.html')
def show_categories(arg1='Список', arg2='категории'):
    if not categories:
        categories = Category.objects.annotate(cnt=Count('service', filter=F('post__is_published'))).filter(cnt__gt=0)
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}