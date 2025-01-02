import requests
from .models import Article
import google.generativeai as genai

def using_gemini(message):

    genai.configure(api_key="AIzaSyCdo42_6KDtvGVqTSnGo3Hblcf9dHnvsdg")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"I am going to give you an article title. Based on that classify it as one "
        f"of the following and map your answer to one of the integers given. DO NOT SAY AN OPTION UNLESS IT IS STATED HERE (only say the classification as an integer nothing else): "
        f"Pro-Democrat: 1, Pro-Republican: 2, Anti-Democrat: 3, Anti-Republican: 4, Neutral: 5"
        f"Title: {message}"
        )
    #use the conten section for more accuarcty 
    return response.text

def updateArticles():

    url = 'https://newsapi.org/v2/everything'
    params = {
        
        'q' : 'republican OR democrat OR trump OR biden',
        'from': '2024-12-23',
        #'category': 'politics',
        'language': 'en',
        'sortBy': 'publishedAt',
        'sources': 'abc-news, bbc-news, bloomberg, cbs-news, cnn, fox-news, the-guardian-uk, the-new-york-times, the-wall-street-journal, the-washington-post ',
        'apiKey': '0aa3b7bdcc1a48539459855d93e33115',
        'page':1,
        'pageSize': 10

    }

    response = requests.get(url, params=params)
    articles = response.json()['articles']

    for article in articles:


        if not Article.objects.filter(article_title = article['title']).exists():

            item = Article(
                article_title = article['title'],
                source = article['source']['name'],
                political_affiliation = using_gemini(article['title']),
                posted_at = article['publishedAt'],
                url = article['url'],
                shownToUser = False,

            )
            print(using_gemini(article['title']))
            item.save()
        
 
        

    ###idea to the issue: send the output to an endpoint and see if it works 
    # there bc this import issue doesnt happen there
    #then look at ur notes for the shell scripts to see the db

if __name__ == '__main__':
    updateArticles()