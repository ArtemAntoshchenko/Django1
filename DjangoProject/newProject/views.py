from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Добро пожаловать на мой сайт!</h1>')

def about_view(request):
    return HttpResponse('<h3>О нас</h3>')

def contact_view(request):
    return HttpResponse('Email:something@gmail.com')

def username_view(request,username):
    return HttpResponse(f'Привет, {username}!')

def article_id_view(request,article_id):
    return HttpResponse(f'Статья №{article_id}')