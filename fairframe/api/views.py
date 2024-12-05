from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#there is where all the api endpoints go

#takes a request and returns a response
def main(request):
    return HttpResponse('bello')
