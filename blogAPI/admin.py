from django.contrib import admin
from .models import Article, Publisher, Categorie, Message

# Register your models here.
admin.site.register(Article)
admin.site.register(Publisher)
admin.site.register(Categorie)
admin.site.register(Message)