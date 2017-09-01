from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ("url", "username", "password",)

class GeoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Geo
		fields = ("lat", "lng",)

class AddressSerializer(serializers.ModelSerializer):
	geo = GeoSerializer(many=False, read_only=True)
	class Meta:
		model = Address
		fields = ("street", "suite", "city", "zipcode", "geo",)

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
	address = AddressSerializer(many=False, read_only=True)
	class Meta:
		model = Perfil
		fields = ("url", "user", "address", )

class PostSerializer(serializers.ModelSerializer):
	perfil = serializers.SlugRelatedField(queryset=Perfil.objects.all(), slug_field="username")
	class Meta:
		model = Post
		fields = ("url", "perfil", "title", "body",)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ("url","post", "name", "email", "body",)

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
	#perfil = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="name")
	comments = CommentSerializer(many=True, read_only=True)
	class Meta:
		model = Post
		fields = ("url", "perfil", "title", "body", "comments")

class PerfilDetailSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostSerializer(many=True, read_only=True)
	class Meta:
		model = Perfil
		fields = ("url","user", "address", "posts")