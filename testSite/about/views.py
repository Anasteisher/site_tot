from django.shortcuts import render
from .models import Product
from .models import DogComment

MENU = {"главная":"/", "о нас":"/about", "блог":"/blog", "отзывы":"/comment"}

def about_page(request):
    products = Product.objects.all()
    title = "О нас"
    data = {"menu":MENU,"title":title, "products": products}
    return render(request, "./about.html", context=data)


def comment_page(request):
    comments = DogComment.objects.filter(checkbox=True)
    title = "Добавить отзыв"
    data = {"menu":MENU,"title":title, "comments": comments}
    return render(request, "./comment.html", context=data)

def thanks_page(request):
    user_name = request.POST['user_name']
    email = request.POST['email']
    feedback = request.POST['feedback']
    checkbox = request.POST.get('checkbox', False)
    DogComment.objects.create(user_name=user_name, email=email, feedback=feedback, checkbox=checkbox)
    title = "Страница виляющих хвостиков"
    data = {"menu":MENU,"title":title, "user_name":user_name}
    return render(request, "./thanks.html", context=data)