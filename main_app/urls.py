from django.urls import path
from main_app.views import *

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('addQuestion/', addQuestion, name = 'addQuesiton'),
    # path('login/', loginPage, name = 'login'),
    # path('logout/', logoutPage, name = 'logout'),
    # path('register/', registerPage, name = 'register'),

]

