from django.urls import path
from .views import getArticles

urlpatterns = [
    path('',getArticles),
]