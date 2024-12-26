from rest_framework.response import Response #returns in JSON form
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework import status

# Create your views here.
#there is where all the api endpoints go

# #takes a request and returns a response
# def main(request):
#     return HttpResponse('bello')

#gives data
@api_view(['GET'])
def getData(request):
    #articles = Article.objects.all()
    articles = {"title": "bdfjbf", "source":"jjjjjj"}
    #serializer = ArticleSerializer(articles ,many=True)
    #return Response(serializer.data)
    return Response(articles)

@api_view(['POST'])
def createData(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

