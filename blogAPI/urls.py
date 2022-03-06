from django.urls import path
from .views import getArticles, sendMessage

urlpatterns = [
    path('',getArticles),
    path('sendMessage',sendMessage)
]