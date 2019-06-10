#f29_createInsertDb_orm.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request
from flask import render_template

app=Flask(__name__)
#définition des tables 
#Pas nécessaire si la base a déjà été créée.

#chemin de la base est celui de l'applicaiton courante
basedir=os.path.abspath(os.path.dirname(__file__))

#nom de la base
bdName=os.path.join(basedir,'laBelleGodasse.db')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+bdName

db=SQLAlchemy(app)


app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True #a cause du message

class Magasins(db.Model):
    __tablename__='magasins'
    id_magasin=db.Column('id_magasin',db.Integer, primary_key=True)
    adresse=db.Column(db.String(64))
    ville=db.Column(db.String(64))
    def __repr__(self):
        return '<Magasins %r>' % self.ville

class Modeles(db.Model):
    __tablename__='modeles'
    id_modeles=db.Column('id_modeles',db.Integer, primary_key=True)
    genre=db.Column(db.String(64))
    type=db.Column(db.String(64))
    prix=db.Column(db.Integer)
    def __repr__(self):
        return '<Modele %r>' % self.genre

class Transactions(db.Model):
     __tablename__='transactions'
     id_transaction=db.Column('id_transaction',db.Integer, primary_key=True)
     id_magasin=db.Column('id_magasin',db.Integer,db.ForeignKey('magasins.id_magasin'))
     id_modele=db.Column('id_modele',db.Integer,db.ForeignKey('modeles.id_modeles'))
     pointure=db.Column('pointure',db.String(64))
     date_transaction=db.Column('date_transaction',db.String(64))
     def __repr__(self):
        return '<Transaction %r>' % self.id_transaction

@app.route('/magasin/<mag>')
def disp_magasin(mag):
    id_magasin = request.args.get('id_magasin', None)
    print(id_magasin)
    mag=Magasins.query.filter(Magasins.id_magasin==id_magasin).first()
    return render_template('f214_un_magasin.html',mag_ville=mag.ville, mag_adresse=mag.adresse, mag_id=mag.id_magasin)


@app.route('/magasins/')
def disp_magasins():
    mags=Magasins.query.all()
    return render_template('f214_magasins.html',magasins=mags)


if __name__=='__main__':
    mag=Magasins.query.all()
    for elt in mag:
        print(elt.ville)
   

    app.run(debug=True)
    #Mise à jour pour la table magasin

    #pour afficher tous les magasins

