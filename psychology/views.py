from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile_User, Post, Comment, User_model
from .serializer import UserSerializer, PostSerializer, CommentSerializer, ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.

class Register_user(APIView):

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Get_User_Profile(APIView):

    def get_user(self, pk):
        try:
            return User_model.objects.get(pk=pk)
        except User_model.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        the_user = self.get_user(pk)
        serializers = UserSerializer(the_user)
        return Response(serializers.data)


class Get_Individual_Post(APIView):

    def get_user(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        the_user = self.get_user(pk)
        serializers = UserSerializer(the_user)
        return Response(serializers.data)


class Post_getter(APIView):

    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment_getter(APIView):

    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_post = Comment.objects.all()
        serializers = CommentSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CommentSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# {"token":"8c3f8c4f2448fd1822d97a0efdf9be9f601365d4"}