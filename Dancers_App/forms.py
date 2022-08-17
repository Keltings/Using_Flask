from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, \
SelectField, validators, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class AddTaskForm(Form):
    task_id = IntegerField()
    dancer_name = StringField('Task Name', validators=[DataRequired()])
    performance_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y'
    )
    genre = SelectField(
        'Genre',
        validators=[DataRequired()],
        choices=[
            ('Salsa', 'Salsa'), ('Kizomba', 'Kizomba'), ('Bachata', 'Bachata'), ('Semba', 'Semba'), ('Hiphop', 'Hiphop'),
            ('African', 'African'), ('Ballet', 'Ballet'), ('B-boy', 'B-boy'), ('Chacha', 'Chacha'), ('Other', 'Other')
        ]
    )
    status = IntegerField('Status')


#cater for both user and loggi
class RegisterForm(Form):
    name = StringField(
        'Username',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match')]
    )   


class LoginForm(Form):
    name = StringField(
        'Username',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )