from flask import Flask
from flask import render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

