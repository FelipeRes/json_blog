import json
import httplib2
import urllib
from pprint import pprint
import requests

headers = {'Content-type': "application/json"}
h = httplib2.Http()
#Inserir Usuario:
def new_user(username, email, password):
	user_data = {
    	"username": username,
    	"email": email,
    	"password": password,
	}
	post_data_format = json.dumps(user_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/user/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	user_url = json.loads(content.decode())

def comment(postId, name, email, text):
	comment_data = {
    	"post": "http://localhost:8000/post/"+str(postId)+"/",
    	"name": name,
    	"email": email,
    	"body": text,
    }
	post_data_format = json.dumps(comment_data,indent=4)
	response, content = h.request(uri="http://localhost:8000/comment/", method="POST", headers=headers, body=post_data_format)
	pprint(response)
	pprint(content)
	print('\n')