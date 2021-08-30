from django.contrib.auth import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from backend.utils import getUserFromHeader


# Create your views here.

class RegistrationAPIView(APIView):
    serializer_class=RegistrationAPISerializer
    def post(self, req):
        ser=RegistrationAPISerializer(data=req.data)
        if ser.is_valid():
            usr_obj = User()
            usr_obj.username = req.data.get("username")
            usr_obj.email = req.data.get("email")
            usr_obj.is_staff = req.data.get("teacher")
            usr_obj.set_password(req.data.get("password"))
            usr_obj.save()
            refresh = RefreshToken.for_user(usr_obj)
            resp_data= {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            return Response(resp_data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

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
