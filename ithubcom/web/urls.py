from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Home'),
    path('users/', our_users, name='Our_users'),
]
