from django.contrib.auth import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission, IsAdminUser
from rest_framework.views import APIView

from api.serializer import *
# Create your views here.

class RegistrationAPIView(APIView):
    serializer_class=RegistrationAPISerializer
    def post(self, req):
        ser=RegistrationAPISerializer(data=req.data)
        if ser.is_valid():
            usr_obj = User()
            usr_obj.username = req.data.get("username")
            usr_obj.email = req.data.get("email")
            usr_obj.is_staff = req.data.get("is_staff")!=None
            usr_obj.set_password(req.data.get("password"))
            usr_obj.save()
            refresh = RefreshToken.for_user(usr_obj)
            resp_data= {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            return Response(resp_data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Users_with_subject(APIView):
    def get(self,request,pk):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        relations = UserSubjectRelation.objects.filter(subject=pk)
        required_relations = paginator.paginate_queryset(relations,request)
        listt = []
        for item in required_relations:listt.append(item.user)
        users = UserInfoSerializer(listt,many = True)
        return paginator.get_paginated_response(users.data)

class Subjects_of_user(APIView):
    def get(self,request,pk):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        relations = UserSubjectRelation.objects.filter(user=pk)
        required_relations = paginator.paginate_queryset(relations,request)
        listt = []
        for item in required_relations:listt.append(item.subject)
        users = SubjectSerializer(listt,many = True)
        return paginator.get_paginated_response(users.data)

class CreateAssignment(APIView):
    def post(self,req):
        try:
            data = req.data
            title = data.get('title')
            subject = data.get('subject')
            try: subject = Subject.objects.get(id=subject)
            except: return Response('subject do not exist', status=status.HTTP_404_NOT_FOUND)
            questions = data.get('questions')
            if type(questions)!=list:
                return Response("questions must be a list",status=status.HTTP_405_METHOD_NOT_ALLOWED)
            assignment_instance = Assignment(title=title,subject=subject)
            assignment_instance.save()
            for item in questions:
                item["assignment"] = assignment_instance.pk
            questions_ser = QuestionSerializer(data=questions,many=True)
            if questions_ser.is_valid():
                questions_ser.save()
            ser = AssignmentSerializer(assignment_instance)
            data = ser.data
            data["questions"] = questions_ser.data
            return Response(data)
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class CreateTest(APIView):
    def post(self,req):
        try:
            data = req.data
            title = data.get('title')
            subject = data.get('subject')
            try: subject = Subject.objects.get(id=subject)
            except: return Response('subject do not exist', status=status.HTTP_404_NOT_FOUND)
            questions = data.get('questions')
            if type(questions)!=list:
                return Response("questions must be a list",status=status.HTTP_405_METHOD_NOT_ALLOWED)
            test_instance = Test(title=title,subject=subject)
            test_instance.save()
            for item in questions:
                item["test"] = test_instance.pk
            questions_ser = QuestionSerializer(data=questions,many=True)
            if questions_ser.is_valid():
                questions_ser.save()
            ser = TestSerializer(test_instance)
            data = ser.data
            data["questions"] = questions_ser
            return Response(data)
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Assignment_of_subject(APIView):
    def get(self,req,pk):
        try:
            assignment = Assignment.objects.get(subject=pk)
            questions = Question.objects.filter(assignment=assignment.id)
            assignment_ser = AssignmentSerializer(assignment)
            questions_ser = QuestionSerializer(questions,many=True)
            return Response({"assignment":assignment_ser.data,"questions":questions_ser.data})
        except Exception as e:
            return Response(str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class getUser(APIView):
    def post(self,req):
        JWT = JWTAuthentication()
        token = req.data.get("token")
        validated_token = JWT.get_validated_token(token)
        user = JWT.get_user(validated_token)
        userser = UserInfoSerializer(user)
        return Response(userser.data)

class TenPerPage(PageNumberPagination):
    page_size = 10

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class SubjectAPIView(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser|ReadOnly]
    pagination_class=TenPerPage
    serializer_class=SubjectSerializer
    queryset=Subject.objects.all()

class AssignmentAPIView(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser|ReadOnly]
    pagination_class=TenPerPage
    serializer_class=AssignmentSerializer
    queryset=Assignment.objects.all()

class TestAPIView(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser|ReadOnly]
    pagination_class=TenPerPage
    serializer_class=TestSerializer
    queryset=Test.objects.all()

class UserSubjectRelationAPIView(viewsets.ModelViewSet):
    pagination_class=TenPerPage
    serializer_class=UserSubjectRelationSerializer
    queryset=UserSubjectRelation.objects.all()
