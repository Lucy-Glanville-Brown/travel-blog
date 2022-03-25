from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """ Form for adding comments to blog post. """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ Form for adding blog posts. """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'excerpt',)
