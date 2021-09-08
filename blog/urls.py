from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('comment/<int:pk>/', add_comment, name='add_comment'),
    path('post/<str:slug>/', PostPage.as_view(), name='post'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
]