from flask import Flask

app = Flask(__name__)
from app import views
#1- create the application obj
#2-and then imports the view module, that is why we have to avoid circular references
