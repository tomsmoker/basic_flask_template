from flask import render_template, url_for

from app import app 

@app.route('/')
@app.route('/index')
def index():
    
    user = {
        'username': "tom"
    }
    
    quotes_i_like = [
        {
            'author': {'username': "mum"},
            'text': "he means well"
        },
        {
            'author': {'username': "kawhi leonard"},
            'text': "i'm a fun guy"
        },
        {
            'author': {'username': "bette midler"},
            'text': "the worst part of success is to try to find someone who is happy for you."
        } 
    ]
    
    return render_template('index.html', title="toms page", user=user, quotes=quotes_i_like)