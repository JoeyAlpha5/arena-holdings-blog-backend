from .models import Article, Publisher, Categorie, Message
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    article_publisher_name = serializers.ReadOnlyField(source='article_publisher.publisher_name')
    article_category_name = serializers.ReadOnlyField(source='article_category.category_name')
    class Meta:
        model = Article
        fields = '__all__'