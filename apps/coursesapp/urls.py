from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_coursesapp_index'),
    url(r'^addcourse$', views.addcourse, name = 'my_coursesapp_addcourse'),
    url(r'^removecourse/(?P<id>\d+)$', views.removecourse, name = 'my_coursesapp_removecourse'),
    url(r'^removethis/(?P<id>\d+)$', views.removethis, name = 'my_coursesapp_removethis'),
    url(r'^index$', views.index, name = 'my_coursesapp_index_route'),
    url(r'^usercourses$', views.usercourse, name = 'my_coursesapp_usercourses'),
]