from django.urls import path
from .views import Create_quiz,Create_question,Create_optione

urlpatterns = [
    path('create_quiz/', Create_quiz.as_view()),
    path('create_question/', Create_question.as_view()),
    path('Create_optione/', Create_optione.as_view())
]
