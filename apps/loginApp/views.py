from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
import datetime

def index(request):
	return render(request, 'loginApp/index.html')

def register(request):
	if User.userManager.register(request.POST, request):
		passFlag = True
		# messages.error(request, "Valid Email!")
		# User.emailManager.create(email=request.POST['userEmail'])
		return redirect('/loginApp')
	else:
		passFlag = False
		# messages.error(request, "Not a valid email")
		return redirect('/loginApp')

def login(request):
	if User.userManager.login(request.POST, request):
		context = {
			"user": User.objects.get(email=request.POST['userEmail'])
		}
		passFlag = True
		# messages.error(request, "Valid Email!")
		# User.emailManager.create(email=request.POST['userEmail'])
		return render(request, 'loginApp/results.html', context)
	else:
		passFlag = False
		# messages.error(request, "Not a valid email")
		return redirect('/loginApp')

def usercourse(request):
	
		return redirect('/loginApp')