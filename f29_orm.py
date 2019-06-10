#f29_orm.py
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)


#chemin de la base est celui de l'applicaiton courante
basedir=os.path.abspath(os.path.dirname(__file__))

#nom de la base
bdName=os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+bdName
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #a cause du message

db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), unique=True)

def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), unique=True, index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

#si la base n'existe pas on la créée
if os.path.isfile(bdName)==False:
    db.create_all()