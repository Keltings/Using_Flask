import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# IMPLEMENT DATABASE URL
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:#Datascience1@localhost:5432/postgres'
DATABASE = 'postgresql.db'
USERNAME = 'postgres'
PASSWORD = '#Datascience1'
