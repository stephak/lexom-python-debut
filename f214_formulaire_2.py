#f214_formulaire_2.py
from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)



@app.route('/')
def render_static():
   name = request.args.get('user_name', None)
   surname=request.args.get('user_surname', None)
   message=request.args.get('user_message', None)
   return render_template('/f214_formulaire_2.html',user_surname=surname, user_name=name, user_message=message)

if __name__ == '__main__':
   app.run(debug = True)