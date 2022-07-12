from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import createUserform, addQuestionform
from .models import QuestionModel


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
            'incorrect' : incorrect,
            'correct' : correct,
            'percent' : percent,
            'total' : total
        }
        return render(request, 'result.html', context)
    else: 
        questions = QuestionModel.objects.all()
        context = {
            'questions' : questions
        }
        return render(request, 'home.html', context)

def addQuestion(request):
    if request.user.is_admin:
        form = addQuestionform()
        if(request.method == 'POST'):
            form = addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'addQuestion.html', context)
    else:
        return redirect('home')

def signup(request):
    error_messages = ''
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
            return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

def login(request): 
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
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
