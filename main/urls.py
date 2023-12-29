from django.urls import path
from .views import *
urlpatterns = [
    path('api/',index,name='index'),
    path('api/<int:id>',delete_question,name='delete'),
    path('api/update/<int:id>',update_question,name='update')
]