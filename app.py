# import the Flask class from the flask package
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify

#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object(__name__)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

# TODO: connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True

#use the decorator pattern to link the view function to a url
@app.route("/")
# define the view using a function, which returns a string
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')    





# start the development server using the run() method
if __name__ == "__main__":
    app.run()    