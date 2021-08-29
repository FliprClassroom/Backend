from django.contrib.auth import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class RegistrationAPIView(APIView):
    serializer_class=RegistrationAPISerializer
    def post(self, req):
        ser=RegistrationAPISerializer(data=req.data)
        if ser.is_valid():
            usr_obj = User()
            usr_obj.username = req.data.get("username")
            usr_obj.email = req.data.get("email")
            usr_obj.set_password(req.data.get("password"))
            usr_obj.save()
            refresh = RefreshToken.for_user(usr_obj)
            resp_data= {
                'access': str(refresh.access_token)
            }
            return Response(resp_data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)