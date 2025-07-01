from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at']

    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete=models.CASCADE, null=True, default=None, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(verbose_name='Изображение', blank=True, null=False, upload_to='media/posts')
    description = models.TextField(verbose_name='Запись')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True, blank=True, default = None, verbose_name='Комментарий')
    tag = models.ForeignKey('Tags', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Тэг')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category']

    category = models.CharField(max_length=50, db_index=True, blank=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.category

class Tags(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['tag']

    tag = models.CharField(max_length=25, db_index=True, blank=True, verbose_name='Тэг')

    def __str__(self):
        return self.tag

class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete=models.CASCADE, null=True, default=None, blank=True)
    comment = models.TextField(verbose_name='Запись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')