from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, blank=False)
    meet_link = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]

class Assignment(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]

class Test(models.Model):
    title = models.CharField(max_length=100, blank=False)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]

class UserSubjectRelation(models.Model):
    user = models.ForeignKey(User,  on_delete=CASCADE)
    subject = models.ForeignKey(Subject, on_delete=CASCADE)
    def __str__(self):
        return self.user.username + " --- " + self.subject.name
    class Meta:
        ordering = ["user"]

# class Question(models.Model):
#     test = models.ForeignKey(Test, on_delete=CASCADE, blank=True)

