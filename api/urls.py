from django.urls import path
from .views import (
    Create_quiz,
    Create_question,
    Create_optione,
    Create_user,
    Create_Result_detail,
    Create_Result,
    Create_topic,
    Quiz_list,
    Topic_list,
    Question_list,
    Users_list,
    User_list,
    Result_list,
    Result_detail_list,
    Option_chict,
    )

urlpatterns = [
    path('create_quiz/', Create_quiz.as_view()),
    path('create_question/', Create_question.as_view()),
    path('create_optione/', Create_optione.as_view()),
    path('create_user/', Create_user.as_view()),
    path('create_result_detail/', Create_Result_detail.as_view()),
    path('create_result/', Create_Result.as_view()),
    path('creat_topic/', Create_topic.as_view()),
    path('quiz_list/', Quiz_list.as_view()),
    path('topic_list/<int:pk>/', Topic_list.as_view()),
    path('question_list/<int:pk>/', Question_list.as_view()),
    path('users_list/', Users_list.as_view()),
    path('user_list/<int:pk>/', User_list.as_view()),
    path('result_list/<int:pk>/', Result_list.as_view()),
    path('result_detail_list/<int:pk>/', Result_detail_list.as_view()),
    path('option_chict/<int:pk>/', Option_chict.as_view())
]
