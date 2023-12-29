from django.shortcuts import render, HttpResponse
from .serializers import QuestionsSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def index(request):
    if request.method == "GET":
        question = Questions.objects.all()
        serilaizer = QuestionsSerializer(question, many=True)

        return Response(serilaizer.data, status=status.HTTP_201_CREATED)
    if request.method == "POST":
        serilaizer = QuestionsSerializer(data=request.data)
        ''' print(request.data) give dictionary '''
        if serilaizer.is_valid():
            serilaizer.save()
        return Response(serilaizer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def delete_question(request, id):
    try:
        question = Questions.objects.get(id=id)
    except Questions.DoesNotExist:
        return Response(
            {"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND
        )

    question.delete()
    return Response(
        {"message": "Question deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )


@api_view(["PUT"])
def update_question(request, id):
    try:
        question = Questions.objects.get(id=id)
    except Questions.DoesNotExist:
        return Response({"error": "no such question exist "})
    serializer = QuestionsSerializer(question, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_question_by_id(request,id):
    try:
        question = Questions.objects.get(id=id)
    except:
        return Response({'message':'question with this id does not exit'},status=status.HTTP_400_BAD_REQUEST)
    serilaizer = QuestionsSerializer(question)
    return Response(serilaizer.data)

    