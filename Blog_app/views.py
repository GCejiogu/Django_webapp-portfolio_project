
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Category, Post
from .serializers import AuthorSerializer, CategorySerializer,PostSerializer

# Create your views here.

class AuthorView(APIView):

    def get (self, request):
        auth1 = Author.objects.all()
        serializer = AuthorSerializer(auth1, many = True)
        return Response (serializer.data)

    def post (self):
        pass

class CategoryView(APIView):

    def get (self, request):
        cat1 = Category.objects.all()
        serializer = CategorySerializer(cat1, many = True)
        return Response (serializer.data)

    def psot (self):
        pass

class PostView(APIView):

    def get (self, request):
        post1 = Post.objects.all()
        serializer = PostSerializer(post1, many =True)
        return Response (serializer.data)

    def post (self):
        pass