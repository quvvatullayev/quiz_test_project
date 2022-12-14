from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
import pprint
from .models import (
    Quiz, 
    Topic, 
    Question, 
    Option, 
    User, 
    Result, 
    Result_detail
)
from .serializers import (
    Quiz_serilaizers, 
    Topic_serilaizers,
    Question_serilaizers,
    Option_serilaizers,
    User_serilaizers,
    Result_serializers,
    Result_detail_serilaizers
)

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Create_quiz(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Quiz_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_topic(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Topic_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_question(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Question_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_optione(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Option_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_user(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = User_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print('error')
        return Response(serializer.errors)

class Create_Result_detail(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Result_detail_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_Result(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Result_serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Quiz_list(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, requset:Request):
        quiz = Quiz.objects.all()
        serilaizer = Quiz_serilaizers(quiz, many = True)
        return Response(serilaizer.data)

class Topic_list(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request:Request, pk):
        quiz_filter = Quiz.objects.get(id = pk)
        quiz = Quiz_serilaizers(quiz_filter, many = False)

        topic_filter = Topic.objects.filter(quiz = quiz.data['id'])
        topic = Topic_serilaizers(topic_filter, many = True)

        data = {
            'quiz':{
                'id':quiz.data['id'],
                'title':quiz.data['title'],
                'topics':topic.data
                }
        }

        return Response(data)

class Question_list(APIView):
    def get(self, request:Request, pk):
        topic_filter = Topic.objects.get(id = pk)
        topic = Topic_serilaizers(topic_filter, many = False)

        quiz_filter = Quiz.objects.get(id = topic.data['quiz'])
        quiz = Quiz_serilaizers(quiz_filter, many = False)

        question_filter = Question.objects.filter(t_name = topic.data['id'])
        question = Question_serilaizers(question_filter, many = True)

        data = {
            "id":quiz.data['id'], 
            'title':quiz.data['title'],
            "topic":{
                'id':topic.data["id"], 
                'topic_name':topic.data['t_name'],
                'question_index_list':list(range(len(question.data))),
                'questions':[]
                }
            }

        for i in question.data:
            option_filter = Option.objects.filter(quetion = i['id'])
            option = Option_serilaizers(option_filter, many = True)
            data['topic']['questions'].append({
                'id':i['id'],
                'question':i['quetion'],
                'topic_id':i['t_name'],
                "optons":option.data
            })

        return Response(data)

class Users_list(APIView):
    def get(self, request:Request):
        user = User.objects.all()
        serilaizer = User_serilaizers(user, many = True)
        data = {
            "user_listis":serilaizer.data
        }
        return Response(data)

class User_list(APIView):
    def get(self, request:Request, pk):
        user = User.objects.get(id = pk)
        serilaizer = User_serilaizers(user, many = False)
        return Response(serilaizer.data)

class Result_list(APIView):
    def get(self, request:Request, pk):
        user = User.objects.get(id = pk)
        result = Result.objects.filter(user_id = user)
        serilaizer1 = User_serilaizers(user, many = True)
        serilaizer2 = Result_serializers(result, many = True)

        data = {
            'user':serilaizer1.data,
            'result':serilaizer2.data
        }

        return Response(data)

class Result_detail_list(APIView):
    def get(self, request:Request, pk):
        resutl = Result.objects.get(id = pk)
        result_detail = Result_detail.objects.filter(result = resutl)

        serilaizer2 = Result_serializers(resutl, many = False)
        serilaizer3 = Result_detail_serilaizers(result_detail, many = True)

        user_id = serilaizer2.data['user_id']
        user = User.objects.get(id = user_id)
        serilaizer1 = User_serilaizers(user, many = False)

        data = {
            'user':serilaizer1.data,
            'result':serilaizer2.data,
            'result_detail':serilaizer3.data
        }
        
        return Response(data)

class Option_chict(APIView):
    def get(self, request:Request, pk):
        option_filter = Option.objects.get(id = pk)
        return Response({"chict":option_filter.is_right})

class Chict_all(APIView):
    def get(self, request:Request, pk, rk):
        result = Result.objects.get(id = rk)
        result_detail = Result_detail.objects.filter(result = result)
        result_detail_serilaizer = Result_detail_serilaizers(result_detail, many = True)
        f = 0
        t = 0
        for i in result_detail_serilaizer.data:
            if i['is_solved'] == False:
                f += 1
            elif i['is_solved'] == True:
                t += 1
        return Response({"True":t, "False":f})



