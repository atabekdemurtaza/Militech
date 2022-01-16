from dataclasses import field
from pyexpat import model
from rest_framework import serializers 
from post.models import Post 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):

	class Meta: 

		model  = Post
		fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

	class Meta:

		model = get_user_model()
		fields = ('id', 'username')