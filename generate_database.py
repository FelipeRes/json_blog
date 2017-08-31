import json
import httplib2
import urllib
from pprint import pprint
import requests

with open('db.json') as data_file:    
    data = json.load(data_file)

#insert users
headers = {'Content-type': "application/json"}
h = httplib2.Http()
for user in data['users']:	
	geo_data = {
		"lat" : user['address']['geo']['lat'],
	    "lng": user['address']['geo']['lng'],
	}
	post_data_format = json.dumps(geo_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/geo/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	geo_url = json.loads(content.decode())
	pprint(geo_url)
	print('\n')

	address_data = {
    	"street": user['address']['street'],
    	"suite": user['address']['suite'],
    	"city": user['address']['city'],
    	"zipcode": user['address']['zipcode'],
    	"geo": geo_url['url'],
	}
	post_data_format = json.dumps(address_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/address/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	address_url = json.loads(content.decode())
	pprint(address_url)
	print('\n')

	user_data = {
		"id" : user['id'],
    	"name": user['name'],
    	"email": user['email'],
    	"address": address_url['url'],
	}
	post_data_format = json.dumps(user_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/user/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	print('\n')
for post in data['posts']:
	post_data = {
		'id' : post['id'],
		'user' : 'http://localhost:8000/user/' + str(post['userId'])+'/',
		'title' : post['title'],
		'body' : post['body'],
	}
	post_data_format = json.dumps(post_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/post/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	print('\n')

for comment in data['comments']:
	comment_data = {
		"id": comment['id'],
    	"post": 'http://localhost:8000/post/'+str(comment['postId'])+'/',
    	"name": comment['name'],
    	"email": comment['email'],
    	"body": comment['body'],
    }
	post_data_format = json.dumps(comment_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/comment/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	print('\n')