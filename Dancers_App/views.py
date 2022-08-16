from distutils.log import error
from flask import Flask, render_template, request, g, Response, session, flash, redirect, url_for, jsonify
from functools import wraps
from forms import AddTaskForm, RegisterForm, LoginForm
from models import Dance, User
from flask_sqlalchemy import SQLAlchemy
import datetime
import os

#configure
#create the application object
app = Flask(__name__, template_folder='templates')

# pulls in app configuration from this module
app.config.from_object('_config')
db = SQLAlchemy(app)
#db.init_app(app)
#migrate = Migrate(app, db)

#connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Datascience1@localhost:5432/application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create a error handling
app.config["DEBUG"] = True

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#route handlers
@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Bye!')
    return redirect(url_for('login'))

#One view mapped to the main url
@app.route('/', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password==request.form['password']:
                session['logged_in'] = True
                session['user_id'] = user.id
                flash('Welcome!')
                return redirect(url_for('tasks')) 
            else: 
                error = 'Invalid username or password.'
                #return render_template('login.html', error=error)
        else:
            error = 'Both fields are required'
            
    return render_template('login.html', form=form, erro=error) 


@app.route('/tasks/')
@login_required
def tasks():
    open_tasks = db.session.query(Dance).filter_by(status='1').order_by(Dance.performance_date.asc())
    closed_tasks = db.session.query(Dance).filter_by(status='0').order_by(Dance.performance_date.asc())
    return render_template(
        'tasks.html',
        form=AddTaskForm(request.form),
        open_tasks=open_tasks,
        closed_tasks=closed_tasks
    )
    


# Add new tasks
@app.route('/add/', methods=['POST', 'GET'])
@login_required
def new_task():
error = False
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                new_task = Dance(
                    form.dancer_name.data,
                    form.performance_date.data,
                    form.genre.data,
                    datetime.datetime.utcnow(),
                    '1',
                    '1',
                    session['user_id']
                )
                db.session.add(new_task)
                db.session.commit()
                flash('New entry was successfully posted. Thanks.')
                return redirect(url_for('tasks'))
            except:
                error = True
                db.session.rollback()
                flash('All fields are required')
            
                print(sys.exc_info())  
            finally:
                db.session.close()
    return redirect(url_for('tasks'))      
    return render_template('tasks.html', form=form)

# Mark tasks as complete
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
    new_id = task_id
    db.session.query(Dance).filter_by(task_id=new_id).update({"status": "0"})
    db.session.commit()
    flash('The task is complete. Nice.')
    return redirect(url_for('tasks'))

# Delete Tasks
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
    new_id = task_id
    db.session.query(Dance).filter_by(task_id=new_id).delete()
    db.session.commit()
    flash('The task was deleted. Why not add a new one?')
    return redirect(url_for('tasks'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate():
            new_user = User(
                form.name.data,
                form.email.data,
                form.password.data,
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
    return render_template('register.html',form=form, error=error)
        