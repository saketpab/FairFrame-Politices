#this takes our models and translate it into a JSON response 
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_title', 'source', 'political_affiliation', 'posted_at','url','shownToUser')


