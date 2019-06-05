from flask import Flask
import getlog
import datetime

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World <h1>'



@app.route('/getlog/')
def get_log():
    date=str(datetime.datetime.now().strftime('%y-%m-%d'))
    chaine=getlog.get_weird_queries('.',"squidAnonymise.db",10)
    return "<h1>STAT SUR SQUID du "+date+"</h1><p>"+str(chaine)+"<p>"


@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    return '<h2>la page n existe pas <h2>'

if __name__=='__main__':
    app.run(debug=True)