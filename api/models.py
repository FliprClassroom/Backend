from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, blank=False)
    meet_link = models.CharField(max_length=300, blank=True)

class Assignment(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)

class Test(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)

class UserSubjectRelation(models.Model):
    user = models.ForeignKey(User,  on_delete=CASCADE)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)