from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    question = models.CharField(max_length = 500, null = True)
    A = models.CharField(max_length = 200, null = True)
    B = models.CharField(max_length = 200, null = True) 
    C = models.CharField(max_length = 200, null = True)
    D = models.CharField(max_length = 200, null = True)
    answer = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.question

