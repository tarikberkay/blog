from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view())
] 
