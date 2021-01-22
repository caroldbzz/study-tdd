from flask import Flask

my_web_app = Flask('my_web_app')

@my_web_app.route('/')
def initial_page():
    return ''