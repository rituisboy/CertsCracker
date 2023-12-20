from django.shortcuts import render, HttpResponse
from .serializers import QuestionsSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET","POST"])
def index(request):
    if request.method == "GET":
        question = Questions.objects.all()
        serilaizer = QuestionsSerializer(question, many=True)

        return Response(serilaizer.data)
    if request.method == "POST":
        serilaizer = QuestionsSerializer(data=request.data)
        if serilaizer.is_valid ():
            serilaizer.save()
        return Response(serilaizer.data,status=status.HTTP_201_CREATED)