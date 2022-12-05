from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
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
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = User_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_Result_detail(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        data = request.data
        serializer = Result_detail_serilaizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Create_Result(APIView):
    permission_classes = [IsAuthenticated]
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
        quiz = Quiz.objects.get(id = pk)
        topic = Topic.objects.filter(quiz = quiz)
        serilaizer1 = Quiz_serilaizers(quiz, many = False)
        serilaizer = Topic_serilaizers(topic, many = True)

        data = {
            'quiz':serilaizer1.data,
            'topic':serilaizer.data
        }

        return Response(data)

class Question_list(APIView):
    def get(self, request:Request, pk):
        topic = Topic.objects.get(id = pk)
        question = Question.objects.filter(t_name = topic)

        serilaizer1 = Topic_serilaizers(topic, many = False)

        pk_quiz = serilaizer1.data.get('quiz')
        quiz = Quiz.objects.get(id = pk_quiz)
        serilaizer2 = Quiz_serilaizers(quiz, many = False)

        serilaizer = Question_serilaizers(question, many = True)

        data = {
            'quiz':serilaizer2.data,
            'topic':serilaizer1.data,
            'question':serilaizer.data
        }


        return Response(data)

class Option_list(APIView):
    def get(self, request:Request, pk):
        question = Question.objects.get(id = pk)
        option = Option.objects.filter(quetion = question)
    
        serilaizer1 = Question_serilaizers(question, many = False)
    
        tupic_id = serilaizer1.data.get('t_name')
        tupic = Topic.objects.get(id = tupic_id)
        serilaizer2 = Topic_serilaizers(tupic, many = False)
    
        quiz_id = serilaizer2.data.get('quiz')
        quiz = Quiz.objects.get(id = quiz_id)
        serilaizer3 = Quiz_serilaizers(quiz, many = False)

        serilaizer4 = Option_serilaizers(option, many = True)

        data = {
            'quiz':serilaizer3.data,
            'topic':serilaizer2.data,
            'question':serilaizer1.data,
            'option':serilaizer4.data
        }

        return Response(data)






