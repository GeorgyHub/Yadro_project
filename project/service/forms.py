from django import forms
from django.forms import ModelForm
from service.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        models = Post
        fields = ['title', 'image', 'description', 'category', 'tag']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }