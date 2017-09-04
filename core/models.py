from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Geo(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()

class Address(models.Model):
	street = models.CharField(max_length=128)
	suite = models.CharField(max_length=128)
	city = models.CharField(max_length=32)
	zipcode = models.CharField(max_length=10)
	geo = models.ForeignKey(Geo)

class Perfil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.ForeignKey(Address)
	
	@property
	def username(self):
		return self.user.username

	@property
	def email(self):
		return self.user.email

	@property 
	def name(self):
		return self.user.name

class Post(models.Model):
	perfil = models.ForeignKey(Perfil, related_name="posts", )
	title = models.CharField(max_length=128)
	body = models.TextField()

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	email = models.EmailField()
	body = models.TextField()

