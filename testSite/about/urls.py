from django.urls import path
from .views import *

urlpatterns = [
    path('', about_page),
    path('comment/', comment_page),
    path('thanks/', thanks_page, name="thanks_page"),
]
