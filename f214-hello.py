#f214_hello.py
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World <h1>'

@app.route('/user/<name>')
def user(name):
    return '<h2>salut<h2>'+ name

@app.errorhandler(404)
def page_not_found(error):
    return '<h2>la page n existe pas <h2>'

if __name__=='__main__':
    app.run(debug=True)
