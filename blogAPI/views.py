from django.shortcuts import render
# import API view and response from django_rest_framework which will be used to display results in the browser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import serializers that will be used to serialize the data
from .serializers import ArticleSerializer
from .models import Article
# Create your views here.

@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all().select_related('article_publisher', 'article_category')
    serialized_articles = ArticleSerializer(articles, many=True)
    return Response(serialized_articles.data)