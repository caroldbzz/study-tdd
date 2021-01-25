from flask import Flask, render_template

my_web_app = Flask('my_web_app')

@my_web_app.route('/')
def initial_page():
    return render_template('home.html')

if __name__ == "__main__":
    my_web_app.run()