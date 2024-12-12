from django.db import models

# Create your models here.

#news articles that will be stores in the database    

#basically a database but in python"""
class Article(models.Model):
    #default varaible is the default value when the model is created
    title = models.CharField(max_length = 50, default = "", unique = True)
    source = models.CharField(max_length = 50, default = "")

    categories = [("Dem", "Democrat"), ('Reb', 'Republican'), ('','')]
    political_affiliation = models.CharField(max_length = 3,choices = categories, default = '')

    posted_at = models.DateTimeField(auto_now_add=True)