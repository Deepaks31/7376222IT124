from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('post/', views.post, name='post'),
    path('feed/', views.feed, name='feed'),
]