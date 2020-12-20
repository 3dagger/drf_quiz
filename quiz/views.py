from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
import random
from .serializers import QuizSerializer
# Create your views here.

@api_view(['GET'])
def helloAPI(reqeust):
    return Response("hello World!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many = True)
    return Response(serializer.data)