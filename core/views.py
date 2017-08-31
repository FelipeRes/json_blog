from django.shortcuts import render
from core.models import *
from core.serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse

# Create your views here.

class GeoList(generics.ListCreateAPIView):
	queryset = Geo.objects.all()
	serializer_class = GeoSerializer
	name ='geo-list'

class GeoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Geo.objects.all()
	serializer_class = GeoSerializer
	name ='geo-detail'

class AddressList(generics.ListCreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	name ='address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	name ='address-detail'

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name ='user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserDetailSerializer
	name ='user-detail'

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name ='post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	name ='post-detail'

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name ='comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name ='comment-detail'