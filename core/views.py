from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.models import *
from core.serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import permissions
from core.permissions import *

# Create your views here.
class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	name ='user-list'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	name ='user-detail'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

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

class PerfilList(generics.ListCreateAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer
	name ='perfil-list'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsPerfilOrReadOnly)

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilDetailSerializer
	name ='perfil-detail'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsPerfilOrReadOnly)

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name ='post-list'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsPostOrReadOnly)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	name ='post-detail'
	permission_classes = ( permissions.IsAuthenticatedOrReadOnly, IsPostOrReadOnly)

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name ='comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name ='comment-detail'

class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'perfils':reverse(UserList.name, request=request),
			'posts':reverse(PostList.name, request=request),
			'comments':reverse(CommentList.name, request=request),
			'users':reverse(UserList.name, request=request),
			})