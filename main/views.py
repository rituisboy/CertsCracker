from django.shortcuts import render, HttpResponse
from .serializers import QuestionsSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET","POST"])
def index(request,id=None):
    if request.method == "GET":
        question = Questions.objects.all()
        serilaizer = QuestionsSerializer(question, many=True)

        return Response(serilaizer.data)
    if request.method == "POST":
        serilaizer = QuestionsSerializer(data=request.data)
        if serilaizer.is_valid ():
            serilaizer.save()
        return Response(serilaizer.data,status=status.HTTP_201_CREATED)
@api_view(['DELETE'])
def delete_question(request, id):
    try:
        question = Questions.objects.get(id=id)
    except Questions.DoesNotExist:
        return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)

    question.delete()
    return Response({'message': 'Question deleted successfully'}, status=status.HTTP_204_NO_CONTENT)