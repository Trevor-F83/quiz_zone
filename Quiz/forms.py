from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createUserform(UserCreationForm):
    class Meta:
        model=Userfields=['username', 'password']

class addQuestionform(ModelForm):
    class Meta:
        model=QuestionModel
        fields='__all__' 