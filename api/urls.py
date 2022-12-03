from django.urls import path
from .views import (
    Create_quiz,
    Create_question,
    Create_optione,
    Create_user,
    Create_Result_detail,
    Create_Result
    )

urlpatterns = [
    path('create_quiz/', Create_quiz.as_view()),
    path('create_question/', Create_question.as_view()),
    path('create_optione/', Create_optione.as_view()),
    path('create_user/', Create_user.as_view()),
    path('create_result_detail/', Create_Result_detail.as_view()),
    path('create_result/', Create_Result.as_view())
]
