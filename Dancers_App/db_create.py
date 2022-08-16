from _config import DATABASE_PATH
from flask import Flask, render_template, request, Response, session, flash, redirect, url_for, jsonify

from views import db
from models import Dance
from datetime import date
#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object('_config')
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True


# create the database and the db table
db.create_all()

# insert data
db.session.add(Dance("Finish this tutorial", date(2016, 9, 22), 10, 1))
db.session.add(Dance("Finish Real Python", date(2016, 10, 3), 10, 1))
# commit the changes
db.session.commit()