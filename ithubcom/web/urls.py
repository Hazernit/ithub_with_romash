from django.urls import path
from .views import *

urlpatterns = [
    path('', registration, name='Home'),
    path('users/', our_users, name='Our_users'),
    path('edit_user/', edit_user, name='Edit_user'),
]
