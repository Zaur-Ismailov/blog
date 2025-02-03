from django.db import models
from .models import *

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, default= 'default.png')
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    likes = models.ManyToManyField('auth.User', related_name='likes')
    dislikes = models.ManyToManyField('auth.User', related_name='dislikes')
    views = models.ManyToManyField('auth.User', related_name='views')

    def __str__(self):
        
        return self.title
    def snippet(self):
        return self.body[:30] + '...'

class Comment(models.Model):
    body=models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)
    likes = models.ManyToManyField('auth.User', related_name='comment_likes')
    dislikes = models.ManyToManyField('auth.User', related_name='comment_dislikes')
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name= 'reply'
    )

    def __str__(self):
        return self.body
 