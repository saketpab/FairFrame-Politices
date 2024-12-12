from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
#there is where all the api endpoints go

# #takes a request and returns a response
# def main(request):
#     return HttpResponse('bello')

#creating an API view that allows us to see all the rooms
#allows to also create articles
class ArticleView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class =  ArticleSerializer
