#14-utilitaire-web-template.py
from flask import Flask,render_template
import f214_getlog as getlog
import datetime

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World <h1>'


@app.route('/getlog2/')
def get_log2():
    date_squid=str(datetime.datetime.now().strftime('%y-%m-%d'))
    contenu_html = str(getlog.get_weird_queries('.', "squidAnonymise.db", 10))
    return render_template('log.html',date_squid=date_squid,contenu_html=contenu_html)


@app.route('/getlog3/')
def get_log3():
    date_squid=str(datetime.datetime.now().strftime('%y-%m-%d'))
    contenu = getlog.get_weird_queries('.', "squidAnonymise.db", 10)
    return render_template('lecture_liste.html',date_squid=date_squid,maListe=contenu)

@app.route('/getlog4/')
def get_log4():
    date_squid=str(datetime.datetime.now().strftime('%y-%m-%d'))
    contenu = getlog.get_weird_queries('.', "squidAnonymise.db", 10)
    return render_template('lecture_liste_extend.html',date_squid=date_squid,maListe=contenu)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__=='__main__':
    app.run(debug=True)



