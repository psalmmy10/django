from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('blogPosts/<str:pk>', views.blogPosts , name = 'blogPosts'),
    # path('about/<str:pk>', views.about , name = 'about')
]
