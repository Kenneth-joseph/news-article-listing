from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    latest_news=get_news('sports')
    latest_news=get_news('')
    print(latest_news)
    message = 'Hello kent joz'
    title = 'Home - Welcome to The best News anchor page'
    return render_template('index.html', message=message, title=title,sports=latest_news)

@app.route('/news/<id>')
def news(id):

    return render_template('news.html',id = id)