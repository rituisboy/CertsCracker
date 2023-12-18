from django.shortcuts import render, HttpResponse
from .serializers import QuestionsSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def index(request):
    question = Questions.objects.all()
    serilaizer = QuestionsSerializer(question, many=True)

    return Response(serilaizer.data)
