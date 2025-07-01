from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Добро пожаловать на мой сайт!</h1>')

def products(request,id):
    if id>0:
        return HttpResponse(f'Товар с ID: {id}')
    elif id<0:
        return HttpResponse("Ошибка: ID должен быть положительным")

def profile(request,username,post_id):
    return HttpResponse(f"Пользователь: {username}, пост №{post_id}")

def greeting(request,name,language="Русский"):
    return HttpResponse(f"Привет, {name}! Язык: {language}")