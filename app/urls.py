from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path("post/<int:pk>/", post, name="post"),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:pk>/', edit_post, name='edit_post' ),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('post_likes/<int:pk>/', post_like, name='post_like'),
    path('post_dislikes/<int:pk>/', post_dislike, name='post_dislike'),
    
]
