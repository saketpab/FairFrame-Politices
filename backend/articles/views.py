from rest_framework.response import Response #returns in JSON form
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework import status
import requests

# Create your views here.
#there is where all the api endpoints go

# #takes a request and returns a response
# def main(request):
#     return HttpResponse('bello')

#gives data
@api_view(['GET'])
def getData(request):



    url = 'https://newsapi.org/v2/everything'
    params = {
        
        'q' : 'republican OR democrat OR trump OR biden',
        'from': '2024-12-23',
        #'category': 'politics',
        'language': 'en',
        'sortBy': 'publishedAt',
        'sources': 'abc-news, bbc-news, bloomberg, cbs-news, cnn, fox-news, the-guardian-uk, the-new-york-times, the-wall-street-journal, the-washington-post ',
        'apiKey': '0aa3b7bdcc1a48539459855d93e33115'
        

    }

    response = requests.get(url, params=params)

    #articles = Article.objects.all()
    articles = {"title": "bdfjbf", "source":"jjjjjj"}
    #serializer = ArticleSerializer(articles ,many=True)
    #return Response(serializer.data)
    return Response(response.json())

@api_view(['POST'])
def createData(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

