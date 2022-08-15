# import the Flask class from the flask package
from distutils.log import error
from flask import Flask, render_template, request, Response, session, flash, redirect, url_for, jsonify
from functools import wraps
#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object('config')
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True

#use the decorator pattern to link the view function to a url
@app.route("/", methods=['GET', 'POST'])
# define the view using a function, which returns a string
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Pleas try again.'
            status_code = 401
        else:
            session['logged_in'] = True  
            return redirect(url_for('main'))
    return render_template('login.html', error=error), status_code        
     
    return render_template('login.html')



#restrict access to the main.html
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap



@app.route('/main')
@login_required
def main():
    return render_template('main.html')  

#function for logging out to app.py:
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("you have been logged out")
    return redirect(url_for('login'))





# start the development server using the run() method
if __name__ == "__main__":
    app.run()    