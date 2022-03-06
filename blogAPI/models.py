from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=200,blank=False,null=False)
    publisher_date_joined = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    # return the name of the publisher in the django admin page
    def __str__(self):
        return self.publisher_name
    # order the list of publishers in the django admin by the date they joined
    class Meta:
        ordering = ['-publisher_date_joined']

# I've name this class Categorie instead of Category because Django will append an 's' to the name of the class
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30,blank=False,null=False)
    category_date_added = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    # return the name of the category in the django admin page
    def __str__(self):
        return self.category_name
    # order the list of categories in the django admin by the date they were added
    class Meta:
        ordering = ['-category_date_added']

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    # an article can only have one publisher
    article_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,blank=False,null=False)
    # an article can only have one category
    article_category = models.ForeignKey(Categorie, on_delete=models.CASCADE,blank=False,null=False)
    article_title = models.CharField(max_length=100,blank=False,null=False)
    article_created_at = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    article_updated_at = models.DateTimeField(auto_now=True,blank=False,null=False)
    article_image_link = models.URLField(blank=False,null=False)
    article_content = models.TextField(blank=False,null=False)
    # return the title of the article in the django admin page
    # the display of the articles table in the django admin page can be altered in admin.py using ModelAdmin.list_display
    def __str__(self):
        return self.article_title
    # order the articles by the date of creation
    class Meta:
        ordering = ['-article_created_at']



class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message_sender_name = models.CharField(max_length=200,blank=False,null=False)
    message_sender_email = models.EmailField(max_length=200,blank=False,null=False)
    message_sender_mobile_number = models.CharField(max_length=200,blank=False,null=False)
    message_content = models.TextField(blank=False,null=False)
    message_date_sent = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    # return the name of the individual sending the message in the django admin page
    def __str__(self):
        return self.message_sender_name
    # order the list of messages in the django admin by the date they were sent
    class Meta:
        ordering = ['-message_date_sent']