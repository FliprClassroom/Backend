
from django.urls import path, include
from rest_framework.views import APIView
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subject', SubjectAPIView, basename='subject')
router.register('assignment', AssignmentAPIView, basename='assignment')
router.register('test', TestAPIView, basename='test')
router.register('usersubject', SubjectAPIView, basename='usersubject')

urlpatterns = [
    path('crud/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegistrationAPIView.as_view(),name='register'),
]