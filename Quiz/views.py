from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuestionModel.objects.all()
        results = 0
        incorrect = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.answer == request.POST.get(q.question):
                results += 10
                correct += 1
            else:
                incorrect += 1 
        percent = results/(total*10) *100
        context = {
            'results' : results,
            'time' : request.POST.get(timer),
            'incorrect' : incorrect,
            'correct' : correct,
            'percent' : percent,
            'total' : total
        }
        return render(request, 'Quiz/result.html', context)
    else: 
        questions = QuestionModel.objects.all()
        contecxt = {
            'questions' : questions
        }
        return render(request, 'Quiz/home.html', context)

def addQuestion(request):
    if request.user.is_admin:
        form = addQuestionform()
        if(request.method == 'POST'):
            form = addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('home')

def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createUserform()
        if request.method == 'POST':
            form = createUserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
            context = {
                'form' : form,
            }        
            return render(request, 'Quiz/register.html', context)

def loginPage(request): 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password')

    user = authenticate(username = 'username', password = 'password')
    if user is not None:
        login(request, user)
        return redirect('/')
    context = {}
    return render(request, 'Quiz/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('/')
