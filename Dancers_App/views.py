from flask import Flask, render_template, request, g, Response, session, flash, redirect, url_for, jsonify
from functools import wraps
from forms import AddTaskForm
from models import Dance
from flask_sqlalchemy import SQLAlchemy

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
    flash('Bye!')
    return redirect(url_for('login'))

#One view mapped to the main url
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('tasks'))
    return render_template('login.html') 


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

    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate():
            new_task = Dance(
                form.dancer_name.data,
                form.performance_date.data,
                form.genre.data,
                '1'
            )
            db.session.add(new_task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
    return redirect(url_for('tasks'))

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
        