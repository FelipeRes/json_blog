from rest_framework import serializers
from core.models import *

class GeoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Geo
		fields = ("url", "lat", "lng",)

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ("url", "street", "suite", "city", "zipcode", "geo",)

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ("url","name","email","address", )

class PostSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="name")
	class Meta:
		model = Post
		fields = ("url", "user", "title", "body",)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ("url","post", "name", "email", "body",)

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="name")
	comments = CommentSerializer(many=True, read_only=True)
	class Meta:
		model = Post
		fields = ("url", "user", "title", "body", "comments")

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostSerializer(many=True, read_only=True)
	class Meta:
		model = User
		fields = ("url","name","email","address", "posts")