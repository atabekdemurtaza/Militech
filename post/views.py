from rest_framework import generics 
from post.models import Post 
from post.serializers import PostSerializer
from post.permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from post.serializers import UserSerializer
from rest_framework import viewsets

#Так как у нас тут 2 контроллера (Post и User) я хочу их обьединить
#Для этого мне нужен viewsets

"""class PostListView(generics.ListCreateAPIView):

	serializer_class = PostSerializer 
	queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = PostSerializer 
	queryset = Post.objects.all()
	permission_classes = (IsAuthorOrReadOnly,)

class UserListView(generics.ListCreateAPIView):

	serializer_class = UserSerializer
	queryset = get_user_model().objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

	serializer_class = UserSerializer
	queryset = get_user_model().objects.all()"""
	
class PostViewSet(viewsets.ModelViewSet):

	serializer_class = PostSerializer 
	queryset = Post.objects.all()
	permission_classes = (IsAuthorOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):

	serializer_class = UserSerializer 
	queryset = get_user_model().objects.all()

	
