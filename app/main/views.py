from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news



# Views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    latest_news=get_news('sports')
    latest_news=get_news('entertainment')
    print(latest_news)
    message = 'Hello kent joz'
    title = 'Home - Welcome to The best News anchor page'
    return render_template('index.html', message=message, title=title,sports=latest_news,entertainment=latest_news)

@main.route('/news/<id>')
def news(id):

    return render_template('news.html',id = id)