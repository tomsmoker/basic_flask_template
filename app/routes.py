from flask import render_template, url_for, flash, redirect

from app import app 

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    
    user = {
        'username': "tom"
    }
    
    quotes_i_like = [
        {
            'author': {'username': "daniel radcliffe (in character)"},
            'text': "hey ron"
        },
        {
            'author': {'username': "betty white"},
            'text': "my mother always used to say, 'the older you get, the better you get. unless you’re a banana.'"
        },
        {
            'author': {'username': "churchill"},
            'text': "give a man a fish and you feed him for a day; teach a man to fish and you shall fight him on the beaches"
        } 
    ]
    
    return render_template('index.html', title="toms page", user=user, quotes=quotes_i_like)

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        flash('login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='sign in', form=form)