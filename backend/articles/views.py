from rest_framework.response import Response #returns in JSON form
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework import status
import requests
from .get_articles import updateArticles
from .models import Article

# Create your views here.
#there is where all the api endpoints go

# #takes a request and returns a response
# def main(request):
#     return HttpResponse('bello')

#gives data
@api_view(['GET'])
def getData(request):

    articles = Article.objects.all()
    articles.delete()

    #print('here in endpt')

    updateArticles()

    articles = Article.objects.all()
    #articles = {"article_title": "bdfjbf", "source":"jjjjjj"}
    serializer = ArticleSerializer(articles ,many=True)
    #print(serializer.data)
    return Response(serializer.data)
    #return Response(updateArticles())

@api_view(['POST'])
def sendData(request):
    serializer = ArticleSerializer(data=request.data)
    affiliation = request.data.get('affiliation')
    print(affiliation)

    if affiliation == "Democratic":
        affNum = "1\\n"
    else:
        affNum = "2\\n"
    print(affNum)
    #print(Article.objects.values_list('political_affiliation', flat=True).distinct())
    #print(Article.objects.values_list('political_affiliation'))

    #resArticles = Article.objects.filter(political_affiliation__contains=affNum)
    #resArticles = Article.objects.filter(political_affiliation__contains=affNum)
    resArticles = Article.objects.filter(political_affiliation__startswith=affNum[0])

    #print(resArticles)
    filteredSerializer = ArticleSerializer(resArticles, many=True)

    res = {
        'filteredArticles': filteredSerializer.data
    }
    #print(res)

    if serializer.is_valid():
        serializer.save()
        return Response(res, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

