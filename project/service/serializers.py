from rest_framework import serializers
from .models import Post, Comment, Category, Tags

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post

    title = serializers.CharField(verbose_name='Заголовок', max_length=50)
    slug = serializers.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = serializers.ImageField(verbose_name='Изображение', blank=True, null=False, upload_to='media/posts')
    description = serializers.TextField(verbose_name='Запись')
    category = serializers.ForeignKey('Category', on_delete=serializers.PROTECT, null=True, verbose_name='Категория')
    created_at = serializers.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = serializers.DateTimeField(auto_now=True, verbose_name='Время изменения')
    tag = serializers.ManyToManyField('Tags', null=True, blank=True, verbose_name='Тэг')
    is_published = serializers.BooleanField(default=True, verbose_name='Публикация')

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category

    category = serializers.CharField(max_length=50, db_index=True, blank=True, verbose_name='Категория')
    slug = serializers.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    created_at = serializers.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = serializers.DateTimeField(auto_now=True, verbose_name='Время изменения')

class TagSerializer(serializers.Serializer):
    class Meta:
        model = Tags

    tag = serializers.CharField(max_length=25, db_index=True, blank=True, verbose_name='Тэг')

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment

    post = serializers.ForeignKey('Post', on_delete=serializers.PROTECT, null=True, blank=True, default=None, verbose_name='Запись')
    comment = serializers.TextField(verbose_name='Запись')
    created_at = serializers.DateTimeField(auto_now_add=True, verbose_name='Время создания')

