from rest_framework import generics
from posts.models import *
from posts.serializers import *


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveDestroyAPIView):  
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


"""
Retrieve, Update ve destroy kullanarak hem silme ve hem de görüntüleme işlevini elde etmiş oluruz.
Retrieve get methodunu, update put ve patch methodunu, destroy ise delete methodunu tanımlıyor. 
"""