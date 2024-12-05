from django.urls import path
from .views import main #the dot is for current directory

urlpatterns = [
    path('',main ) #if the path is nothing, go to api.urls
    #it then calls main function thazt we just imported
]