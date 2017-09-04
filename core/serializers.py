from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	#garante a hash do password
	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		instance.set_password(password)
		instance.save()
		return instance

	def update(self, instance, validated_data):
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			else:
				setattr(instance, attr, value)
		instance.save()
		return instance

	class Meta:
		model = User
		fields = ("url", "id", "username", "email", "password")

class GeoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Geo
		fields = ("url", "id", "lat", "lng",)

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ("url", "id", "street", "suite", "city", "zipcode", "geo",)

class PostSerializer(serializers.HyperlinkedModelSerializer):
	#perfil = serializers.SlugRelatedField(queryset=Perfil.objects.all(), slug_field="username")
	class Meta:
		model = Post
		fields = ("url", "perfil", "title", "body",)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ("url","post", "name", "email", "body",)

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
	#perfil = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="name")
	#comments = CommentSerializer(many=True, read_only=True)
	class Meta:
		model = Post
		fields = ("url", "perfil", "title", "body", "comments")

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Perfil
		fields = ("url", "id", "user", "address",)

class PerfilDetailSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostSerializer(many=True, read_only=True)
	class Meta:
		model = Perfil
		fields = ("url", "id", "user", "address", "posts")