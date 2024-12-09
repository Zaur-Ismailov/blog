from django.db import models
from .models import *
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, default= 'default.png')
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE, default = 1)
    
    def __str__(self):
        
        return self.title
    def snippet(self):
        return self.body[:30] + '...'

