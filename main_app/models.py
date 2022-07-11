from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    question_text = models.CharField(max_length = 500, null = True)
    optionA = models.CharField(max_length = 200, null = True)
    optionB = models.CharField(max_length = 200, null = True) 
    optionC = models.CharField(max_length = 200, null = True)
    optionD = models.CharField(max_length = 200, null = True)
    answer = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.question

