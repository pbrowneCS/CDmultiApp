from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request,'turtles/index.html')

def ninja(request):
	context = {
		"blue": '../../static/turtles/img/leonardo.jpg',
		"orange": '../../static/turtles/img/michelangelo.jpg',
		"red": '../../static/turtles/img/raphael.jpg',
		"purple": '../../static/turtles/img/donatello.jpg'
	}
	return render(request, 'turtles/displayNinja.html', context)

def turtleDisplay(request, turtle):
	if turtle == "blue":
		context = {
			'blue': 'turtles/img/leonardo.jpg'
		}
	elif turtle == "orange":
		context = {
			'orange': 'turtles/img/michelangelo.jpg'
		}
	elif turtle == "red":
		context = {
			'red': 'turtles/img/raphael.jpg'
		}
	elif turtle == "purple":
		context = {
			'purple': 'turtles/img/donatello.jpg'
		}
	else:
		context = {
			'april': 'turtles/img/notapril.jpg'
		}
	return render(request, 'turtles/displayNinja.html', context)