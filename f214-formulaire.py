
#f214_formulaire.py
from flask import Flask, redirect, url_for, request
from flask import render_template
app = Flask(__name__)




@app.route('/f214_destination_premier_formulaire.html/')
def render_static3():
    name=request.args.get('user_name',None)
    if name:
        return render_template('/f214_destination_premier_formulaire.html',user_name=name)
    else:
        return render_template('/f214_destination_premier_formulaire.html',user_name='bel inconnu')


@app.route('/')
def render_static2():
    return render_template('/f214_premier_formulaire.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('f214_page_not_found.html'), 404


if __name__ == '__main__':
   app.run(debug = True)