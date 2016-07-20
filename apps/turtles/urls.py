from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index,  name = 'my_turtles_index'),
	url(r'^ninjas/$', views.ninja, name = 'my_turtles_ninjas'),
	url(r'^ninjas/(?P<turtle>\w+)/$', views.turtleDisplay, name = 'my_turtles_ninjas_color')
]