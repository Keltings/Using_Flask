from _config import DATABASE_PATH
from flask import Flask, render_template, request, Response, session, flash, redirect, url_for, jsonify

from views import db
from models import Dance
from datetime import date
#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object('_config')


#connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True


# create the database and the db table
db.create_all()

# insert data
db.session.add(Dance("Jane Ngori", date(2016, 9, 22), "Kizomba", 1))
db.session.add(Dance("Lulu Hassan", date(2016, 10, 3), "Batchata", 1))
# commit the changes
db.session.add(Dance("Bass John", date(2013,9,2), "Salsa", "Kizomba"))
db.session.commit()