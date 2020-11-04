from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile_User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    Username = serializers.CharField(max_length=100)
    Email = serializers.EmailField()
    password = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_User
        fields = ('Profile_pic', 'User_bio',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_post',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment',)