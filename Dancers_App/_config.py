import os
#The SECRET_KEY config setting is used in conjunction 
# with the WTF_CSRF_ENABLED setting in order to create a cryptographic 
# token that is used to validate a form
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:#Datascience1@localhost:5432/application'
DATABASE = 'postgresql.db'
#USERNAME = 'postgres'
#PASSWORD = '#Datascience1'

#makes the app more secure
WTF_CSRF_ENABLED = True


#defines the full path for the db
DATABASE_PATH = os.path.join(basedir, DATABASE)