import requests
from articles.models import Article

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
        'pageSize': 25

    }

    response = requests.get(url, params=params)
    articles = response.json()['articles']

    for article in articles:


        if not Article.objects.filter(title = article['title']).exists():

            item = Article(
                title = article['title'],
                source = article['source']['name'],
                #pol_afil
                posted_at = article['publishedAt'],
                url = article['url']
            )

        item.save()







if __name__ == '__main__':
    updateArticles()