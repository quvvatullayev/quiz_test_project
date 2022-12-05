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
        quiz = Quiz.objects.filter(id = pk)
        topic = Topic.objects.filter(quiz = quiz[0])
        serilaizer1 = Quiz_serilaizers(quiz[0], many = False)
        serilaizer = Topic_serilaizers(topic, many = True)

        return Response([serilaizer1.data,serilaizer.data])

class Question_list(APIView):
    def get(self, request:Request, pk):
        topic = Topic.objects.filter(id = pk)
        question = Question.objects.filter(t_name = topic[0])
        serilaizer1 = Topic_serilaizers(topic[0], many = False)
        serilaizer = Question_serilaizers(question, many = True)

        return Response([serilaizer1.data,serilaizer.data])






