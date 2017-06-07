#1- The views are the handlers that respond to request from web browser or other clients.
#2- Handlers are .py functions
#3- Each view function is mapped to one or more request URLs
#4- Decorators at lines 8 & 9 create the mapping from URLs / and /index to this functions
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
