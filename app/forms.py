from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']


class CommentForm(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={'class':'input', 'placeholder': 'Введите текст комментария...'}))
    
    class Meta:
        model = Comment
        fields = ['body']