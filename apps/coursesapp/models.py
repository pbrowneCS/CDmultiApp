from __future__ import unicode_literals
from django.db import models
from ..loginApp.models import User

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_id = models.ManyToManyField(User)