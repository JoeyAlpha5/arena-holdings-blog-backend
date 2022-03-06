from django.shortcuts import render
# import API view and response from django_rest_framework which will be used to display results in the browser
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import serializers that will be used to serialize the data
from .serializers import ArticleSerializer, MessageSerializer
from .models import Article
# Create your views here.

@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all().select_related('article_publisher', 'article_category')
    serialized_articles = ArticleSerializer(articles, many=True)
    return Response(serialized_articles.data)

@api_view(['POST'])
def sendMessage(request):
    serialized_message = MessageSerializer(data=request.data)
    if serialized_message.is_valid():
        serialized_message.save()

    return Response(serialized_message.data)
    