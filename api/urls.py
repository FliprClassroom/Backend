
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
router.register('usersubject', UserSubjectRelationAPIView, basename='usersubject')

urlpatterns = [
    path('crud/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegistrationAPIView.as_view(),name='register'),
    path('users_with_subject/<int:pk>/',Users_with_subject.as_view()),
    path('subjects_of_user/<int:pk>/',Subjects_of_user.as_view()),
    path('create_assignment/',CreateAssignment.as_view()),
    path('answer_assignment/',AnswerAssignment.as_view()),
    path('create_test/',CreateTest.as_view()),
    path('answer_test/',AnswerTest.as_view()),
    path('assignment_of_subject/<int:pk>/',Assignment_of_subject.as_view()),
    path('questions_of_assignment/<int:pk>/',QuestionsOfAssignment.as_view()),
    path('questions_of_assignment_with_answer/<int:pk>/',QuestionsOfAssignmentWithAnswers.as_view()),
    path('getuser/', getUser.as_view())
]