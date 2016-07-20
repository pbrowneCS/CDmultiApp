from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re
import bcrypt

email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def register(self, userInfo, request):
		passFlag = True
		password = userInfo['password']
		if len(userInfo['firstName']) < 1:
			messages.error(request, "First name cannot be empty.")
			passFlag=False
		if len(userInfo['lastName']) < 1:
			messages.error(request, "Last name cannot be empty.")
			passFlag=False
		if len(userInfo['userEmail']) < 1:
			messages.error(request, "Email cannot be empty.")
			passFlag=False
		if not email_REGEX.match(userInfo['userEmail']):
			messages.error(request, "Email must be a valid format.")
			passFlag=False
		if len(User.objects.filter(email=userInfo['userEmail'])) > 0:
			messages.error(request, "This is already a registered email.")
			passFlag = False
		if len(userInfo['password']) < 1:
			messages.error(request, "Password cannot be empty.")
			passFlag=False
		if len(userInfo['confirm']) < 1:
			messages.error(request, "Password cannot be empty.")
			passFlag=False
		if userInfo['password'] != userInfo['confirm']:
			messages.error(request, "Passwords must match.")
			passFlag=False
		if passFlag == True:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			messages.success(request, "You've successfully registered!")
			User.objects.create(email = userInfo['userEmail'], first_name = userInfo['firstName'], last_name = userInfo['lastName'], password = hashed)
		return passFlag

	def login(self, userInfo, request):
		passFlag = False
		if len(User.objects.filter(email=userInfo['userEmail'])) > 0:
			hashed = User.objects.get(email = userInfo['userEmail']).password
			hashed = hashed.encode('utf-8')
			password = userInfo['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				messages.success(request, "You figured out how to login.")
				passFlag = True
		return passFlag

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	# Connect an instance of UserManager to our User model!
	objects = models.Manager()