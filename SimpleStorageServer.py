#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import shutil

HOST = "127.0.0.1"
PORT = 8888

class SimpleStorageServerRequestHandler(BaseHTTPRequestHandler):
	def __init__(self):
		self.user_passwd = {}
		self.user_files = {}

	def register(self, username, password):
		'''register a user with username and password'''
		if username and passwd and \
		   len(username) > 3 and len(username) < 20 and \
		   str(username).isalnum() and len(password) >= 8:
			self.user_passwd[username] = password
			return True

		if not username:
			print "Invalid: username is empty"
		elif len(username) <= 3 or len(username) >= 20:
			print "Invalid: length of username is not between 3 and 20"
		elif not str(username).isalnum():
			print "Invalid: username contains non alphanumeric characters"
		elif not passwd:
			print "Invalid: password is empty"
		elif len(password) < 8:
			print "Invalid: password is less than 8 characters"
        
		return False

	def login(self, username, password):
		if not self.user_passwd.get(username):
			print "username does not exist!"
			return False
		elif self.user_passwd[username] == password:
			print "success!"
			return True
		else:
			print "password is not correct!"
			return False

	def getFile(self, username, filename):
		filePath = self.user_files.get(username)
		if filePath:
			filePath += filename
			if os.path.isfile(filePath):
				return filePath

	def getFileList(self, username):
		filePath = self.user_files.get(username)
        	if filePath:
			return os.listdir(filePath)

	def putFile(self, username, file):
		filePath = self.user_files.get(username)
		if filePath:
			shutil.copy(file, filePath)

	def deleteFile(self, username, filename):
		filePath = self.user_files.get(username)
		if filePath:
            		filePath += filename
			os.remove(filePath)

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')

if __name__ == "__main__":
	server = HTTPServer((HOST, PORT), SimpleStorageServerRequestHandler)
	print "Starting server " + HOST + " on port ", PORT 
	
	'''wait for http requests'''
	server.serve_forever()

