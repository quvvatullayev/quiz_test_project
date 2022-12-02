from rest_framework import serializers
from api.models import *

class Quiz_serilaizers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class Question_serilaizers(serializers.ModelSerializer):
    class Meta:
        title = serializers.PrimaryKeyRelatedField(slug_field='title', queryset=Quiz.objects.all())
        model = Question
        fields = '__all__'

class Option_serilaizers(serializers.ModelSerializer):
    class Meta:
        question_id = serializers.PrimaryKeyRelatedField(slug_field = 'id', queryset=Question.objects.all())
        model = Question
        fields = '__all__'
        
class User_serilaizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Result_detail_serilaizers(serializers.ModelSerializer):
    class Meta:
        user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all)
        model = Result_detail
        fields = '__all__'

class Result_serializers(serializers.ModelSerializer):
    class Meta:
        user_id = serializers.PrimaryKeyRelatedField(slug_field = 'id', queryset=User.objects.all())
        result_detail_id = serializers.PrimaryKeyRelatedField(slug_field = 'id', queryset=Result_detail.objects.all())
        model = Result
        fields = '__all__'