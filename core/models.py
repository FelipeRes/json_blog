from django.db import models

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

class User(models.Model):
	name = models.CharField(max_length=256)
	email = models.EmailField()
	address = models.ForeignKey(Address)

class Post(models.Model):
	user = models.ForeignKey(User, related_name="posts")
	title = models.CharField(max_length=128)
	body = models.TextField()

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments")
	name = models.CharField(max_length=256)
	email = models.EmailField()
	body = models.TextField()

