from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная":"/", "о нас":"/about", "блог":"/blog", "отзывы":"/comment"}

def main_page(request):
    title = "Главная страница"
    data = {"menu":MENU,"title":title}
    return render(request, "./index.html", context=data)

def blog_page(request):
    title = "Блог"
    data = {"menu":MENU,"title":title}
    return render(request, "./blog.html", context=data)

def comment_page(request):
    title = "О нас"
    data = {"menu":MENU,"title":title}
    return render(request, "./comment.html", context=data)

