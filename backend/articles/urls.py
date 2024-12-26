

#urlpatterns = [
#    path('home',ArticleView.as_view() ) #if the path is nothing, go to api.urls
#]

from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.getData),
    path('/sum', views.createData)
]