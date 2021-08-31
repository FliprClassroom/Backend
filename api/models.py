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

choice = ((1,'option 1'), (2,'option 2'), (3,'option 3'), (4,'option 4'))
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=CASCADE, blank=True, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=CASCADE, blank=True, null=True)
    question = models.CharField(max_length=1000, blank=False)
    option1 = models.CharField(max_length=1000, blank=False)
    option2 = models.CharField(max_length=1000, blank=False)
    option3 = models.CharField(max_length=1000, blank=False)
    option4 = models.CharField(max_length=1000, blank=False)
    answer = models.IntegerField(choices=choice)
    def __str__(self):
        return self.question
    class Meta:
        ordering = ["pk"]
        
class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=CASCADE , null=True)
    question = models.ForeignKey(Question, on_delete=CASCADE, null=True)
    answer = models.IntegerField(choices=choice, null=True)
    def __str__(self):
        return self.answer
    class Meta:
        ordering = ["pk"]