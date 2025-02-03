from django.urls import path
from .views import *

urlpatterns=[
    path('login/', log_in, name = 'log_in'),
    path('logout/', log_out, name = 'logout'),
    path('register/', register, name = 'register'),
    path('', home, name='user_home'),
    path('user_home/', Show_users, name='Show_users')
]