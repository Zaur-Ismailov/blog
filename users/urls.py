from django.urls import path
from .views import *

urlpatterns=[
    path('login/', log_in, name = 'log_in'),
    path('logout/', log_out, name = 'logout'),
    path('register/', register, name = 'register'),

]