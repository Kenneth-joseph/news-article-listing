from app import app
from .models import news
import urllib.request,json


News = news.News

apiKey = app.config['NEWS_API_KEY'] 
base_url = app.config["NEWS_API_URL"]

def get_news(category):
    get_news_url= base_url.format(category,apiKey)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results= None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results


def process_results(new_list):

    news_results= []
    for news_item in new_list:
        id= news_item.get('id')
        name=news_item.get('name')
        author=news_item.get('author')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        publishedAt=news_item.get('publishedAt')
        content=news_item.get('content')

        if content:
            news_responds=News(id,name,author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_responds)

    return news_results            




