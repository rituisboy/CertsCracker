from django.db import models

# Create your models here.


    
class Questions(models.Model):
    questions = models.CharField(max_length=255,null=True)
    optionD = models.CharField(max_length=255,null=True)
    optionA = models.CharField(max_length=255,null=True)
    optionB = models.CharField(max_length=255,null=True)
    optionC = models.CharField(max_length=255,null=True)
    correct = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.questions