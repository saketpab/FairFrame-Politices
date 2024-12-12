from django.urls import path
from .views import ArticleView #the dot is for current directory

urlpatterns = [
    path('home',ArticleView.as_view() ) #if the path is nothing, go to api.urls
]