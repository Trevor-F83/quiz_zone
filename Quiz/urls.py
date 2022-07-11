from django.urls import path
from Quiz.views import *

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addQuestion/', addQuestion, name = 'addQuesiton'),
    path('login/', loginPage, name = 'login'),
    path('logout/', logoutPage, name = 'logout'),
    path('registration/', registrationPage, name = 'registration'),

]

