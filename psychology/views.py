from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile_User, Post, Comment
from .serializer import UserSerializer, PostSerializer, CommentSerializer, ProfileSerializer

# Create your views here.

class Post_getter(APIView):
    
    def get(self, request, format=None):
        all_merch = Post.objects.all()
        serializers = PostSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        
