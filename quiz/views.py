from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

@api_view(['Get'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
# 주어진 갯수만큼 랜덤한 퀴즈를 반환하는 api
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)
    serializers = QuizSerializer(randomQuiz, many=True) #many=True 옵션 추가시 다수의 데이터에 대해서 직렬화 가능
    return Response(serializers.data)