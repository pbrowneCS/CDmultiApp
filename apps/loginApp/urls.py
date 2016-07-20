from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'my_loginApp_index'),
	url(r'^register$', views.register, name = 'my_loginApp_register'),
	url(r'^login$', views.login, name = 'my_loginApp_login'),
	url(r'^usercourse$', views.usercourse, name = 'my_loginApp_usercourse')
]