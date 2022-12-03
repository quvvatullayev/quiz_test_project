from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
from .models import *
from .serializers import *

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
        serializer = Topic_cerilaizers(data=data)
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