#from views import db
from flask import Flask, render_template, request, g, Response, session, flash, redirect, url_for, jsonify
from functools import wraps
from forms import AddTaskForm
import datetime
#from models import Task
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#configure
#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object('_config')
db = SQLAlchemy(app)
#db.init_app(app)
migrate = Migrate(app, db)

#connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True

class Dance(db.Model):
    __tablename__ = "dance"
    task_id = db.Column(db.Integer, primary_key=True)
    dancer_name = db.Column(db.String(120), nullable=False)
    performance_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, dancer_name, performance_date, genre, status,posted_date,user_id):
        self.name = dancer_name
        self.due_date = performance_date
        self.priority = genre
        self.status = status
        self.user_id = user_id
        self.posted_date = posted_date
    def __repr__(self):
        return '<name {0}>'.format(self.name)

#
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('Dance', backref='poster')
    
    def __init__(self, name=None, email=None, password=None, tasks=None):
        self.name = name
        self.email = email
        self.password = password
        #self.tasks = tasks
    def __repr__(self):
        return '<User {0}>'.format(self.name)

db.create_all()

