from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class RegistrationAPISerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ("username","password","email","is_staff")

class StudentInfoSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ("id","username","email","is_staff")

class SubjectSerializer(serializers.ModelSerializer):
   class Meta:
      model = Subject
      fields = "__all__"

class AssignmentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Assignment
      fields = "__all__"

class TestSerializer(serializers.ModelSerializer):
   class Meta:
      model = Test
      fields = "__all__"

class UserSubjectRelationSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserSubjectRelation
      fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Question
      fields = "__all__"
