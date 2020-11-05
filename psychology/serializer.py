from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile_User, Post, Comment, User_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_model
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'