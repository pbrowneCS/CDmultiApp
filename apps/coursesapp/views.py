from django.shortcuts import render, redirect
from .models import Course
from django.core.urlresolvers import reverse
from ..loginApp.models import User
from django.db.models import Count


# Create your views here.
def index(request):
    context = { "courses" : Course.objects.all()}
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect(reverse('my_coursesapp_index'))

def removecourse(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'coursesapp/remove.html', context)

def removethis(request, id):
    this = Course.objects.get(id=id)
    this.delete()
    return redirect(reverse('my_coursesapp_index'))

def usercourse(request):
    if request.method == 'POST':
        our_user = User.objects.get(id = request.POST['user'])
        our_course = Course.objects.get(id = request.POST['course'])
        our_course.user_id.add(our_user)
        our_course.save()
        print our_user
        print our_course.user_id
    c = Course.objects.annotate(num_users=Count('user_id'))
    for x in c:
        print x.user_id.all()
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
        "count": c
    }
    # if request.method == 'POST':
    #     our_user = User.objects.get(id = request.POST['user'])
    #     our_course = Course.objects.get(id = request.POST['course'])
    #     our_course.user_id = Course.objects.get(id = request.POST['user'])
    #     our_course.save() 
    # c = Course.objects.annotate(num_users=Count('user_id'))
    # context = {
    #     "users": User.objects.all(),
    #     "courses": Course.objects.all(),
    #     "count": c,
    # }
    return render(request, 'coursesapp/usercourses.html', context)