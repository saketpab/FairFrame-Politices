from django.db import models

# Create your models here.

#news articles that will be stores in the database    

#basically a database but in python"""
class Article(models.Model):
    #default varaible is the default value when the model is created
    article_title = models.CharField(max_length = 50, default = "")
    source = models.CharField(max_length = 50, default = "")

    categories = [(1, "Democrat"), (2, 'Republican'),(3, 'Neutral')]
    political_affiliation = models.CharField(max_length = 3,choices = categories, default = 0)
    url = models.URLField(default = "")
    posted_at = models.DateTimeField(auto_now_add=True)
    shownToUser = models.BooleanField(default = False)
    description = models.CharField(max_length = 500, default = "")

    #Pro-Democrat, Pro-Republican, Anti-Democrat, Anti-Republican, Neutral
    #"Pro-Democrat: 1, Pro-Republican: 2, Anti-Democrat: 3, Anti-Republican: 4, Neutral: 5"