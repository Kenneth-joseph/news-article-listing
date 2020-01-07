from flask import render_template
from app import app


# Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    message = 'Hello kent joz'
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', message=message, title=title)

