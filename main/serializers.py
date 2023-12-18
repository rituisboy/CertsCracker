from rest_framework import routers, serializers, viewsets
from .models import Questions

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        