from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    title = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quetion = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.title

class Option(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    is_right = models.BooleanField()
    def __str__(self) -> str:
        return self.option

class User(models.Model):
    ferst_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=12)
    admin = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.ferst_name

class Result_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=255)
    is_solved = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.question_name

class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=255)
    result_detail_id = models.ForeignKey(Result_detail, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.quiz_title