from django.contrib import admin
from .models import Post, Comment, Category, Tags

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title', 'category')
    list_filter = ('id', 'title', 'category')
    search_fields = ('title', 'category', 'created_at')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    prepopulated_fields = {"slug": ("category",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')

# Output models
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment, CommentAdmin)